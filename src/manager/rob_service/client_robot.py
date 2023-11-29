import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = "127.0.0.1"
port = 4000
client_socket.connect((host_ip,port))


while True:
    a = input("msg")
    if (a == "sair"):
        client_socket.close()
        break


class robot():
    pass