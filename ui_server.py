#!/usr/bin/env python3
import http.server
import socketserver
import os
import webbrowser

alive = True
message = None


def is_alive():
    return alive


def run():

    return_dir = os.getcwd()
    os.chdir("uiserver")

    with socketserver.TCPServer(("", 0), CustomRequestHandler) as httpd:
        address = "http://localhost:{}".format(httpd.server_address[1])
        try:
            webbrowser.open_new(address)
            print("Launching interface")
        except webbrowser.Error:
            print("Browse to {} to access the interface".format(address))
        while is_alive():
            httpd.handle_request()

    os.chdir(return_dir)
    return eval(message)


class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        global alive
        global message

        content_length = int(self.headers["Content-Length"])
        message = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Signal server loop to terminate itself.
        alive = False

    # Be quiet!
    def log_message(self, format, *args):
        return
