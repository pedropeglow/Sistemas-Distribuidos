from threading import Thread
import socket

listaClientes = []

def enviarMsg(listaClientes):
    while True:
        mensagem = input("Mensagem: ")
        for cli in listaClientes:
            cli.sendall(bytes(mensagem, "utf-8"))

HOST = ''
PORT = 5600

threadEnviaMsg = Thread(target=enviarMsg, args=[listaClientes])
threadEnviaMsg.start()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
    ss.bind((HOST,PORT))
    ss.listen(1)
    while True:
        conn, addr = ss.accept()
        listaClientes.append(conn)

