from socket import *
#Matriz de IPs (Local)
#matriz_dns = [
#    ["somalia", "10.0.84.183"],
#    ["egito", "10.0.84.185"],
#

#Matriz de IPs (Local)
matriz_dns = [
    ["www.matchup.com.br", "127.0.0.2"],
    ["www.youtube.com","127.0.0.3"],
    ["www.ufca.edu.br","127.0.0.4"],
]

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", 50000))

print("Servidor DNS rodando...")

while True:
    #Recebe a mensagem do cliente
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