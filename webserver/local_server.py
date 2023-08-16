import http.server
import socketserver


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    """_summary_
        Only serves index.html files in directories
    """

    def do_GET(self):
        if self.path.startswith('/'):  # hmm it looks like it always starts with '/'

            # This server is only serving index.html files inside the httpdocs folder
            if self.path == '/':
                self.path = 'index.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Create an object of the above class
handler_object = MyHttpRequestHandler

# Start the server
HOST = 'localhost'
PORT = 80

print("Server starting on http://%s:%s" % (HOST, PORT))

web_server = socketserver.TCPServer((HOST, PORT), handler_object)
try:

    web_server.serve_forever()

except KeyboardInterrupt:
    # This does not seem to ALWAYS work - seems OK after successfully serving a web page.
    # Stop the web server
    web_server.server_close()
    print("The server is stopped.")
