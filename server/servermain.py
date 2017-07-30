import socket

HOST = ""
PORT = 54321

def restart():
    global s, conn, addr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    s.listen(5)
    conn, addr = s.accept()
    print("Connected by {0} on port {1}".format(*addr))

    conn.send("Reserved vars: HOST, PORT, s, conn, addr, data".encode())

restart()

while True:
    try:
        data = conn.recv(4096).decode()

        if data == "SHUTDOWN":
            break
        elif data == "RESTART":
            conn.close()
            restart()
        else:
            eval(data)
    except:
        break

conn.close()
