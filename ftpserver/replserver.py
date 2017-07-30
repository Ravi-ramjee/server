import socket


PASSPHRASE = ""
DELIMITER = "`"
HOST = socket.gethostbyname(socket.gethostname())
PORT = 54001
BUFF_SIZE = 4069

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))


def run():
    global s, client, addr, cont

    s.listen(1)
    client, addr = s.accept()
    print("Connected by {0} on port {1}.".format(*addr))

    while True:
        cprint("Passphrase:")
        data = cinput()

        if data == PASSPHRASE:
            cprint("Correct")
            break
        else:
            cprint("Incorrect passphrase, try again.")


    while True:
        try:
            data = cinput()

            if data == "quit":
                print("Disconnecting.")
                break
            elif data == "shutdown":
                print("Shutting down.")
                cont = False
                break
            else:
                exec(data)
        except:
            cprint("Error.")


def cprint(x):
    print(x)
    client.sendall((str(x) + DELIMITER).encode())


def cinput():
    client.sendall(("/INPUT" + DELIMITER).encode())
    data = client.recv(BUFF_SIZE).decode()
    print(">", data)
    return data


cont = True

while cont:
    try:
        run()
    except:
        break

s.close()
