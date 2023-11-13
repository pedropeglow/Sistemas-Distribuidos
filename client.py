# Echo client program
import socket
import json

HOST = 'localhost'
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    autenticacao = {'matricula': matricula, 'senha': senha}
    cliente.send(json.dumps(autenticacao).encode())
    response = cliente.recv(1024).decode()
    if response == "ok":
        print("Autenticação bem-sucedida!")
        menu = cliente.recv(1024).decode()
        print("Cardápio:")
        print(menu)
        escolha = input("Escolha o produto que deseja comprar: ")
        cliente.send(escolha.encode())
        pedido = cliente.recv(1024).decode()
        print(pedido)
    else:
        print("Autenticação falhou. Encerrando conexão.")
        cliente.close()
   
