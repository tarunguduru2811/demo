"""Minimal dependency-free HTTP server built on the Python 3 standard library."""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


def route(path):
    """Dispatch a request to its handler.

    Returns the JSON-serialisable body for the response. New routes should be
    registered here.
    """
    return {"error": "not found"}


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, status, body):
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        self._send_json(404, route(self.path))

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
