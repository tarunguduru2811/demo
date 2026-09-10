"""End-to-end tests for the demo HTTP server."""

import json
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer

import app


class ServerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def request(self, method, path):
        req = urllib.request.Request(
            f"http://127.0.0.1:{self.port}{path}", method=method
        )
        try:
            with urllib.request.urlopen(req) as resp:
                return resp.status, resp.headers["Content-Type"], resp.read()
        except urllib.error.HTTPError as exc:
            return exc.code, exc.headers["Content-Type"], exc.read()

    def test_get_health(self):
        status, content_type, body = self.request("GET", "/health")
        self.assertEqual(status, 200)
        self.assertEqual(content_type, "application/json")
        self.assertEqual(json.loads(body), {"status": "ok"})

    def test_post_health_method_not_allowed(self):
        status, _, _ = self.request("POST", "/health")
        self.assertEqual(status, 405)

    def test_put_health_method_not_allowed(self):
        status, _, _ = self.request("PUT", "/health")
        self.assertEqual(status, 405)

    def test_unknown_path_not_found(self):
        status, _, _ = self.request("GET", "/unknown")
        self.assertEqual(status, 404)


if __name__ == "__main__":
    unittest.main()
