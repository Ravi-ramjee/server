import socket
import time


HOST = ""
PORT = 54321
BUFFSIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))





s.close()




