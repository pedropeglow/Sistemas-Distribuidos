# Echo server program
import socket
import time
import json

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
usuarios = [
    {"matricula": "632020046", "senha": "123", "saldo": 15},
    {"matricula": "632020041", "senha": "1234", "saldo": 10}
]
produtos = [
    {"id": "1", "nome": "Salgado", "valor": 10},
    {"id": "2", "nome": "Refrigerante", "valor": 8},
    {"id": "3", "nome": "Trident", "valor": 4},
    {"id": "4", "nome": "Bolo no Pote", "valor": 4},
    {"id": "5", "nome": "Milk Shake", "valor": 16}
]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:

    def verificaMatriculaSenha(matricula, senha):
        for usuario in usuarios:
            if usuario["matricula"] == matricula and usuario["senha"] == senha:
                return usuario
        return None
    
    def retornaSaldo(matricula):
        for usuario in usuarios:
            if usuario["matricula"] == matricula:
                return usuario["saldo"]
        return None
    
    def retornaValorProduto(produtoEscolhido):
        for produto in produtos:
            if produto["id"] == produtoEscolhido:
                return produto["valor"]
        return None
    
    def atualizaSaldo(matricula, novoSaldo):
        for usuario in usuarios:
            if usuario['matricula'] == matricula:
                usuario['saldo'] = novoSaldo
                return usuario['saldo']
        return None
    
    def verificaCompra(produtoEscolhido):
        for produto in produtos:
            if produto['id'] == produtoEscolhido:
                if produto['valor'] <= saldoUsuario:
                    return produto['nome']
        return None
    



    servidor.bind((HOST, PORT))
    servidor.listen(1)
    while True:
        print("Aguardando conexão...")
        cliente, addr = servidor.accept()
        with cliente:
            print('Connected by', addr)
            time.sleep(2)
            while True:
                autenticacao = cliente.recv(1024).decode()
                autenticacao = json.loads(autenticacao)
                if(verificaMatriculaSenha(autenticacao['matricula'], autenticacao['senha'])):
                    cliente.send("ok".encode())
                    menu = "1. Salgado - R$10\n2. Refrigerante 2L - R$8\n3. Trident - R$4\n4. Bolo no Pote - R$4\n5. Milk Shake - R$16"
                    saldoUsuario = retornaSaldo(autenticacao['matricula'])
                    saldo = f'\033[0;30;42mSeu saldo é: R${saldoUsuario}\033[m\n'
                    cliente.send(saldo.encode())
                    cliente.send(menu.encode())

                    produtoEscolhido = cliente.recv(1024).decode()
                    print(f"Produto Escolhido: {produtoEscolhido}")
                    compra = verificaCompra(produtoEscolhido)
                    if compra:
                        saldoAtualizado = atualizaSaldo(autenticacao['matricula'], saldoUsuario - retornaValorProduto(produtoEscolhido))
                        pedidoMessage = f"Você comprou o produto: {compra}, seu saldo agora é de R${saldoAtualizado}"
                        cliente.send(pedidoMessage.encode())
                    else:
                        error = "Erro ao comprar produto, verifique seu saldo ou se está digitando um produto corretamente!"
                        cliente.send(error.encode())               
                    if not autenticacao: break
                else:
                    cliente.send("not_ok".encode())
                    servidor.close()
                    cliente.close()
               
