# Echo client program
import socket
from threading import Thread

def receberPedido(cliente):
    while True:
        pedido = cliente.recv(1024).decode()
        print(pedido)

HOST = 'localhost'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    t1 = Thread(target=receberPedido, args=[s])
    t1.start()        
    
    while True:
        data = s.recv(1024)
        print('Receive: ', repr(data))
