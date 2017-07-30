import socket


HOST = socket.gethostbyname(socket.gethostname())
PORT = 54002
BUFF_SIZE = 4069

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))


try:
    s.listen(1)
    host, addr = s.accept()
    print(host.recv(BUFF_SIZE).decode())
except:
    print("Error")
finally:
    s.close()
