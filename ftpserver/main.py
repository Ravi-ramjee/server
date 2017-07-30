import server
import serverhandler


PORT = 54000

h = serverhandler.ServerHandler()
s = server.Server(h)
s.bind(port=PORT)
print("Host IP is", s.host)
s.runForever()

