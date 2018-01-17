import GCEServer


HOST = ""
PORT = 11429

server = GCEServer.Server(HOST, PORT)

server.start()
