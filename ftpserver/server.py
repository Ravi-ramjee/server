import socket


class Server (object):
    def __init__(self, handler, backlog=5, buffSize=4096):
        self.handler = handler
        self.backlog = backlog
        self.buffSize = buffSize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ""
        self.port = 0

    def bind(self, host=socket.gethostbyname(socket.gethostname()), port=0):
        self.host = host
        self.port = port
        self.sock.bind((host, port))

    def runForever(self):
        self.sock.listen(self.backlog)

        client, addr = self.sock.accept()
        print("Connected by {0} on port {1}.".format(*addr))

        while True:
            try:
                res = self.handler.handle(client, client.recv(self.buffSize))
                if res:
                    print("Error.")
                    client.send("Error.".encode())
            except socket.error:
                print("Connection error.")
                break

        print("Closing.")
        self.sock.close()
