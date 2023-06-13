from socket import *

#Matriz de 
matriz_dns = [
    ["somalia", "10.0.84.183"],
    ["egito", "10.0.84.185"],
]

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(("127.0.0.1", 50000))

print("Servidor DNS rodando...")

while True:
    message, address = serverSocket.recvfrom(1024)
    name_server = message.decode()
    
    aux = False
    for linha in matriz_dns:
        if linha[0] == name_server:
            serverSocket.sendto(linha[1].encode(), address)
            aux = True
            break
    
    if aux == False:
        serverSocket.sendto("Name Server não encontrado".encode(), address)