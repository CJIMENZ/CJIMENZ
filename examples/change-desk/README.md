# Change desk

Request a change from inside a running app and watch the new revision appear in the same window. The example app is a fictional harbor notice board. Try changing its title, then look at the Git commit that put your words on the page.

## Run it

Use Python 3.10+ and Git on macOS, Linux, or WSL. From this example directory, start the desk in one terminal.

```sh
python3 relay.py init
python3 relay.py serve
```

Open **http://127.0.0.1:8765**, type **Rename to Marina updates**, and queue the change. It stays queued until a worker connects. In a second terminal in the same directory, run the worker.

```sh
python3 relay.py worker
```

The worker edits the source in its own checkout, commits, and pushes. Once the preview shows the new title, inspect the change yourself.

```sh
git -C .relay-demo/checkout show HEAD
python3 -m unittest -v
```

The built-in editor understands “Rename to …” and “Make it blue/green/purple/orange”. For free-form requests about the title or color, stop that worker and start `python3 relay.py worker --claude` with an installed, signed-in Claude Code CLI. The adapter passes the current page source and request to the model, validates its proposed edit, and uses the same commit and deployment path. The deterministic mode runs offline.

## Why put a broker in the middle?

The web app can accept requests while the machine with the checkout is asleep. It writes a message to a durable mailbox and returns immediately. The worker makes outbound requests, so the web app needs neither inbound access to the developer machine nor Git credentials. A deployment receipt ties what the user sees back to a specific revision.

| Stage | Original pilot | Public example |
| --- | --- | --- |
| Request | A phone Dev tab sent a message, optionally with screenshots, to a Neon mailbox. | A browser sends a change request to an HTTP broker backed by SQLite. |
| Edit | A Mac worker polled the mailbox and ran Claude Code in a dedicated clone. | A single worker polls the broker and edits the demo repository. Requests survive worker downtime. |
| Check and push | The development flow called for type checking and a build before a push to GitHub. | The worker validates the change and pushes an actual commit to a local bare Git remote. A pre-receive hook checks the incoming revision. |
| Deploy and report | A Git push triggered Vercel. The worker watched deployment status and checked the running revision as a fallback. | A post-receive hook builds the accepted revision and atomically replaces the served page. The worker reports “live” after matching the preview revision to its pushed commit. |

The local remote and hooks stand in for hosted Git and CI/CD. Each checkout is generated from synthetic data. The example runs on loopback and supports a single worker. Its editing surface is the notice board's title and accent. Expanding it into a shared service would require user authentication, isolated workspaces, and a deployment target per project.

## Read the implementation

- [Broker, worker, Git hooks and renderer](relay.py)
- [Request desk and preview](desk.html)
- [End-to-end test](test_relay.py)
