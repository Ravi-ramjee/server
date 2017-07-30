import socket, sys
from Framework.Client import *
from Framework.Execution import *


class Server(object):
    def __init__(self, hostname, port, path="bin/", max_capacity=10, connect_buffer=2, connection_timeout=0.01):
        self.hostname = hostname
        self.port = port
        self.path = path
        self.max_capacity = max_capacity
        self.connect_buffer = connect_buffer
        self.connection_timeout = connection_timeout
        self.socket = None
        self.clients = []
        self.alive = True
        self.permissions = ROOT

        try:
            startup_commands = open(self.path + 'startup.txt').readlines()
            for command in startup_commands:
                args = command.replace('\n', '').split(' ')
                print(run_command(self, self, args[0], args[1:]))
        except FileNotFoundError:
            print('No startup file detected!')

    def start(self):
        try:
            self.socket = socket.socket()
            self.socket.setblocking(True)
            self.socket.settimeout(self.connection_timeout)
            self.socket.bind((self.hostname, self.port))
            self.socket.listen(self.connect_buffer)
        except OSError:
            print('Operating System Error')
            sys.exit(1)

        self.run()

    def run(self):
        while self.alive:
            try:  # Checks for any clients waiting to connect
                if len(self.clients) < self.max_capacity:
                    conn, addr = self.socket.accept()
                    print("Connection from", addr)
                    conn.settimeout(self.connection_timeout)
                    client = Client(conn, addr)
                    self.clients.append(client)
            except TimeoutError:
                pass
            except OSError:
                pass

            delete_list = []
            for client in self.clients:
                data = b''
                success = False
                while True:
                    try:
                        data += client.recv(4096)
                        success = True
                    except ConnectionError:
                        delete_list.append(client)
                        client.disconnect()
                        print("Disconnection by", client.addr)
                        success = False
                        break
                    except socket.timeout:
                        break

                data = data.decode()
                if success:
                    print(client.get_name() + ': ' + data)
                    data = data.split(' ')
                    reply = run_command(self, client, data[0], data[1:])
                    client.send(reply.encode())

            for client in delete_list:
                self.clients.remove(client)

    def send(self, client, data):
        client.send(data)

    def send_to_all(self, data):
        for client in self.clients:
            client.send(data)

    def get_permissions(self):
        return self.permissions

    def get_name(self):
        return '[Server]'

    def shutdown(self):
        for client in self.clients:
            client.disconnect()
        self.alive = False
