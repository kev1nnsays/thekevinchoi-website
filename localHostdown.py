import threading
try: 
  from http.server import HTTPServer, BaseHTTPRequestHandler # Python 3
except ImportError: 
  import SimpleHTTPServer
  from BaseHTTPServer import HTTPServer # Python 2
  from SimpleHTTPServer import SimpleHTTPRequestHandler as BaseHTTPRequestHandler
server = HTTPServer(('localhost', 0), BaseHTTPRequestHandler)
thread = threading.Thread(target = server.serve_forever)
thread.deamon = True
def up():
  thread.start()
  print('starting server on port {}'.format(server.server_port))
def down():
  server.shutdown()
  print('stopping server on port {}'.format(server.server_port))
