# webserver engines

# buitin http web server (pure python solution)

from http.server import HTTPServer, CGIHTTPRequestHandler
import cgitb; cgitb.enable
CGIHTTPRequestHandler.cgi_directories = ['/web']
#SimpleHTTPRequestHandler

webServer = HTTPServer(("localhost", 8000),CGIHTTPRequestHandler)
print("starting server ...")
webServer.serve_forever()


