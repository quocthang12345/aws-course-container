from http.server import BaseHTTPRequestHandler, HTTPServer
import os, socket

VERSION = os.environ.get("APP_VERSION", "v1")

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200); self.end_headers(); self.wfile.write(b"ok"); return
        body = f"Xin chao tu container {VERSION} - build 1 - host {socket.gethostname()}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers(); self.wfile.write(body)

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
