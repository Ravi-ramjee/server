import socket
from Framework.Permission import *


class Client(object):
    def __init__(self, connection, address, attributes=[]):
        self.conn = connection
        self.addr = address
        self.attributes = {}

        self.permission = Permission(0)

    def send(self, data):
        self.conn.sendall(data)

    def recv(self, buffer):
        return self.conn.recv(buffer)

    def get_permissions(self):
        return self.permission

    def get_name(self):
        if 'name' not in self.attributes:
            self.attributes['name'] = str(self.addr)
        return self.attributes['name']

    def disconnect(self):
        self.conn.shutdown(socket.SHUT_RDWR)