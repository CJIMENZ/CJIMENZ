"""A loopback demo of an in-app change request, Git worker, and push-to-deploy pipeline."""
import argparse
import fcntl
import html
import json
import os
from pathlib import Path
import re
import secrets
import shlex
import sqlite3
import subprocess
import sys
import tempfile
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import Request, urlopen

SOURCE = Path(__file__).resolve()
SITE = Path(__file__).with_name("desk.html")
DEFAULT = {"title": "Harbor notices", "accent": "#185c58"}
COLORS = {"blue": "#245fb2", "green": "#185c58", "purple": "#70469a", "orange": "#a0471e"}


def git(folder, *args):
    return subprocess.run(["git", "-C", str(folder), *args], check=True,
                          capture_output=True, text=True, timeout=30).stdout.strip()


def validate(page):
    if not isinstance(page, dict) or set(page) != {"title", "accent"}:
        raise ValueError("The page needs a title and an accent.")
    if not isinstance(page["title"], str) or not 1 <= len(page["title"].strip()) <= 80:
        raise ValueError("Use a title of 1 to 80 characters.")
    if not isinstance(page["accent"], str) or not re.fullmatch(r"#[a-fA-F0-9]{6}", page["accent"]):
        raise ValueError("Use a six-digit hex color.")
    return page


def read_page(state, revision):
    return validate(json.loads(git(state / "origin.git", "show", revision + ":page.json")))


def publish(state, revision):
    page = read_page(state, revision)
    document = f"""<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(page['title'])}</title>
<body style="font:18px system-ui;background:#f5f2e9;color:#252824;margin:0">
<main style="border-top:12px solid {page['accent']};padding:2rem">
<small>FIELD STATION / NOTICE BOARD</small><h1 style="color:{page['accent']}">{html.escape(page['title'])}</h1>
<p>East pier opens at sunrise.</p><p>Community sail · Saturday, 10 am</p>
<footer data-revision="{revision}">Deployed revision <code>{revision[:10]}</code></footer></main></html>"""
    with tempfile.NamedTemporaryFile(mode="w", dir=state, delete=False) as f:
        f.write(document)
    os.replace(f.name, state / "live.html")


def init(state):
    state.mkdir(mode=0o700, parents=True)  # Require a fresh demo directory.
    origin = state / "origin.git"
    checkout = state / "checkout"
    git(state, "init", "--bare", "-b", "main", str(origin))
    git(state, "clone", str(origin), str(checkout))
    git(checkout, "config", "user.name", "Preview worker")
    git(checkout, "config", "user.email", "preview@example.invalid")
    hook = origin / "hooks" / "post-receive"
    command = shlex.join([sys.executable, str(SOURCE), "--state", str(state), "deploy"])
    hook.write_text('#!/bin/sh\nset -eu\nwhile read -r old new ref; do\n  if [ "$ref" = refs/heads/main ]; then\n    ' + command + ' "$new"\n  fi\ndone\n')
    hook.chmod(0o700)
    check = origin / "hooks" / "pre-receive"
    verify = shlex.join([sys.executable, str(SOURCE), "--state", str(state), "check"])
    check.write_text('#!/bin/sh\nset -eu\nwhile read -r old new ref; do\n  test "$ref" = refs/heads/main\n  ' + verify + ' "$new"\ndone\n')
    check.chmod(0o700)
    (checkout / "page.json").write_text(json.dumps(DEFAULT, indent=2) + "\n")
    git(checkout, "add", "page.json")
    git(checkout, "commit", "-m", "Create fictional harbor notice board")
    git(checkout, "push", "origin", "HEAD:main")
    if not (state / "live.html").is_file():
        raise RuntimeError("Initial deployment did not produce the preview.")
    (state / "worker.key").write_text(secrets.token_urlsafe(32))
    with db(state) as conn:
        conn.execute("""CREATE TABLE jobs (id INTEGER PRIMARY KEY, message TEXT NOT NULL,
                     status TEXT NOT NULL DEFAULT 'queued', detail TEXT NOT NULL DEFAULT '')""")


def db(state):
    return sqlite3.connect(state / "queue.db", timeout=10)


def change(repo, page, message, use_claude):
    if use_claude:
        prompt = ("Edit the fictional notice board. Return only JSON with title and accent "
                  "(six-digit CSS hex). Keep fields unchanged unless requested. Current source: "
                  + json.dumps(page) + "\nChange request: " + message)
        result = subprocess.run(["claude", "-p", "--tools", "", "--no-session-persistence", prompt],
                                cwd=repo, capture_output=True, text=True, check=True, timeout=120)
        return validate(json.loads(result.stdout))
    title = re.fullmatch(r"rename to (.+)", message, re.I)
    if title:
        return validate({**page, "title": title[1].strip()})
    color = re.fullmatch(r"make it (blue|green|purple|orange)", message, re.I)
    if color:
        return {**page, "accent": COLORS[color[1].lower()]}
    raise ValueError("Try ‘Rename to Marina updates’ or ‘Make it purple’.")


def handle_job(state, job, use_claude):
    repo = state / "checkout"
    marker = f"Apply request {job['id']}"
    if git(repo, "log", "-1", "--format=%s") != marker:
        current = json.loads(git(repo, "show", "HEAD:page.json"))
        updated = validate(change(repo, current, job["message"], use_claude))
        (repo / "page.json").write_text(json.dumps(updated, indent=2) + "\n")
        git(repo, "add", "page.json")
        git(repo, "commit", "--allow-empty", "-m", marker)
    revision = git(repo, "rev-parse", "HEAD")
    git(repo, "push", "origin", "HEAD:main")
    if git(state / "origin.git", "rev-parse", "main") != revision:
        raise ValueError("Remote revision differs from the worker commit.")
    if f'data-revision="{revision}"' not in (state / "live.html").read_text():
        raise ValueError("Push accepted, but deployment was not confirmed.")
    return revision


def serve(state, port):
    class Handler(BaseHTTPRequestHandler):
        def reply(self, status, data, mime="application/json"):
            self.send_response(status)
            self.send_header("Content-Type", mime + "; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write((json.dumps(data) if mime == "application/json" else data).encode())

        def do_GET(self):
            if self.path in ("/", "/preview"):
                path = SITE if self.path == "/" else state / "live.html"
                return self.reply(200, path.read_text(), "text/html")
            if self.path == "/jobs":
                with db(state) as conn:
                    conn.row_factory = sqlite3.Row
                    rows = conn.execute("SELECT * FROM jobs ORDER BY id DESC LIMIT 20")
                    return self.reply(200, [dict(row) for row in rows])
            self.reply(404, {})

        def do_POST(self):
            if self.headers.get("Host") != f"127.0.0.1:{port}":
                return self.reply(403, {})
            if self.path == "/jobs":
                if self.headers.get("Origin") != f"http://127.0.0.1:{port}":
                    return self.reply(403, {})
            elif self.headers.get("Authorization") != "Bearer " + (state / "worker.key").read_text():
                return self.reply(403, {})
            try:
                size = int(self.headers.get("Content-Length", "0"))
                if not 0 < size <= 8192:
                    return self.reply(400, {})
                payload = json.loads(self.rfile.read(size))
                with db(state) as conn:
                    if self.path == "/jobs":
                        message = payload["message"].strip()
                        if not 1 <= len(message) <= 500:
                            return self.reply(400, {})
                        conn.execute("INSERT INTO jobs(message) VALUES (?)", (message,))
                    elif self.path == "/claim":
                        conn.execute("BEGIN IMMEDIATE")
                        job = conn.execute("SELECT id,message FROM jobs WHERE status IN ('working','queued') ORDER BY id LIMIT 1").fetchone()
                        if job:
                            conn.execute("UPDATE jobs SET status='working' WHERE id=?", (job[0],))
                        conn.commit()
                        return self.reply(200, {"id": job[0], "message": job[1]} if job else None)
                    elif self.path == "/finish":
                        if payload["status"] not in ("live", "failed"):
                            return self.reply(400, {})
                        conn.execute("UPDATE jobs SET status=?,detail=? WHERE id=? AND status='working'",
                                     (payload["status"], payload["detail"], payload["id"]))
                    else:
                        return self.reply(404, {})
            except (ValueError, KeyError, TypeError, AttributeError):
                return self.reply(400, {})
            self.reply(200, {"ok": True})

    print(f"Open http://127.0.0.1:{port}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()


def worker(state, port, use_claude, once):
    key = (state / "worker.key").read_text()
    def post(path, payload):
        request = Request(f"http://127.0.0.1:{port}/{path}", json.dumps(payload).encode(),
                          {"Authorization": "Bearer " + key, "Content-Type": "application/json"})
        with urlopen(request, timeout=10) as response:
            return json.load(response)

    with (state / "worker.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        while True:
            job = post("claim", {})
            if job:
                try:
                    detail = handle_job(state, job, use_claude)
                    status = "live"
                except (ValueError, OSError, subprocess.SubprocessError) as exc:
                    detail = str(exc) if isinstance(exc, ValueError) else type(exc).__name__
                    status = "failed"
                post("finish", {"id": job["id"], "status": status, "detail": detail})
            if once:
                return
            time.sleep(0.6)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=Path(".relay-demo"))
    parser.add_argument("--port", type=int, default=8765)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init")
    commands.add_parser("serve")
    run = commands.add_parser("worker")
    run.add_argument("--claude", action="store_true")
    run.add_argument("--once", action="store_true")
    commands.add_parser("deploy").add_argument("revision")
    commands.add_parser("check").add_argument("revision")
    args = parser.parse_args()
    state = args.state.resolve()
    if args.command == "init":
        init(state)
    elif args.command == "serve":
        serve(state, args.port)
    elif args.command == "worker":
        worker(state, args.port, args.claude, args.once)
    elif args.command == "check":
        read_page(state, args.revision)
    else:
        publish(state, args.revision)
