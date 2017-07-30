import socket


class ServerHandler (object):
    def __init__(self):
        self.cmds = {
            "echo": self.echo,
            # "login": self.login,
        }

    def handle(self, sock, cmd):
        try:
            cmd = cmd.decode().split()
            self.cmds[cmd[0]](sock, *cmd[1:])
        except:
            return -1

    def echo(self, sock, *args):
        sock.sendall(" ".join(args).encode())

    def login(self, sock, username, password):
        pass

