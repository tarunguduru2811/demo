"""Minimal dependency-free HTTP server built on the Python 3 standard library."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def route(method, path):
    """Dispatch a request to its handler.

    Returns a ``(status, body)`` tuple describing the response; ``body`` is the
    JSON-serialisable payload. New routes should be registered here.
    """
    if path == "/health":
        if method == "GET":
            return 200, {"status": "ok"}
        return 405, {"error": "method not allowed"}
    return 404, {"error": "not found"}


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, status, body):
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def __getattr__(self, name):
        # Route every HTTP method (GET, POST, PUT, ...) through the router so
        # unsupported methods on a known path still get a 405.
        if name.startswith("do_"):
            return self._handle
        raise AttributeError(name)

    def _handle(self):
        status, body = route(self.command, self.path)
        self._send_json(status, body)

    def log_message(self, format, *args):
        pass


def main():
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer(("", port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
