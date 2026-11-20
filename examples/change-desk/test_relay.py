"""End-to-end smoke test using a real queue, clone, push and deployment hook."""
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from urllib.error import URLError
from urllib.request import Request, urlopen

import relay


class DeliveryTest(unittest.TestCase):
    def test_offline_queue_to_live_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            state = Path(tmp) / "demo"
            with socket.socket() as sock:
                sock.bind(("127.0.0.1", 0))
                port = sock.getsockname()[1]
            base = f"http://127.0.0.1:{port}"
            cmd = [sys.executable, str(relay.SOURCE), "--state", str(state), "--port", str(port)]
            subprocess.run(cmd + ["init"], check=True)
            server = subprocess.Popen(cmd + ["serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            def request(path, data=None):
                body = json.dumps(data).encode() if data is not None else None
                with urlopen(Request(base + path, body, {"Origin": base}), timeout=2) as r:
                    return r.read().decode()
            try:
                for attempt in range(60):
                    try:
                        self.assertIn("Queue change", request("/"))
                        break
                    except URLError:
                        time.sleep(.05)
                request("/jobs", {"message": "Rename to Marina updates"})
                self.assertEqual(json.loads(request("/jobs"))[0]["status"], "queued")
                subprocess.run(cmd + ["worker", "--once"], check=True)
                job = json.loads(request("/jobs"))[0]
                self.assertEqual(job["status"], "live")
                self.assertEqual(job["detail"], relay.git(state / "origin.git", "rev-parse", "main"))
                preview = request("/preview")
                self.assertIn(job["detail"], preview)
                self.assertIn("Marina updates", preview)
                request("/jobs", {"message": "Unsupported edit"})
                subprocess.run(cmd + ["worker", "--once"], check=True)
                self.assertEqual(json.loads(request("/jobs"))[0]["status"], "failed")
                self.assertEqual(request("/preview"), preview)
            finally:
                server.terminate()
                server.wait(timeout=5)
