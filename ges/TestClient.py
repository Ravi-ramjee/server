import socket
import _thread
import time


HOST = "areeb.mynetgear.com"
PORT = 11429
BUFFSIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def send_to():
    while True:
        try:
            data = input("> ").encode()
            s.sendall(data)
            if data.decode() == "quit":
                print("closing")
                break
        except ConnectionError:
            print('Server not responding')
            break


def receive_from():
    while True:
        try:
            data = s.recv(BUFFSIZE)
            print(data.decode())
        except ConnectionError:
            print('Server not responding')
            break

try:
    _thread.start_new_thread(send_to, ())
except:
    print('Error while starting thread.')

receive_from()

s.close()
