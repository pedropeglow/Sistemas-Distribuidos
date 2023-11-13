import socket

HOST = 'localhost'
PORT = 5600

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        print('Recebido: ', repr(data))