import GCEServer


HOST = "192.168.0.11"
PORT = 11429

server = GCEServer.Server(HOST, PORT)

server.start()