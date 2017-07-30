import socket


class Server (object):
    def __init__(self, handler, buffSize=4096):
        self.handler = handler
        self.buffSize = buffSize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ""
        self.port = 0

    def bind(self, host=socket.gethostbyname(socket.gethostname()), port=0):
        self.host = host
        self.port = port
        self.sock.bind((host, port))

    def runForever(self, backlog=5):
        self.sock.listen(backlog)

        client, addr = self.sock.accept()
        print("Connected by {0} on port {1}.".format(*addr))

        while True:
            try:
                data = client.recv(self.buffSize).decode()
                print("> " + data)

                if data == "quit":
                    self.sock.close()
                    break

                client.send(data.encode())
                print(data)
            except socket.error:
                print("Error receiving data.")
                break

        print("Closing.")
        self.sock.close()


s = Server()
s.bind(port=54321)
print("Host IP is", s.host)
s.runForever(1)
