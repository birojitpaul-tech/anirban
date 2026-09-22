from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class SiteHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("", "/"):
            self.send_response(302)
            self.send_header("Location", "/Home.dc.html")
            self.end_headers()
            return
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 5000), SiteHandler).serve_forever()