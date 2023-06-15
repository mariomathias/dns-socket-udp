# MATCHUP
from socket import *

# Cria o socket UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Define o endereço e a porta do socket
serverSocket.bind(('127.0.0.2', 8000))

print("Servidor ligado...")

while True:
    # Recebe o pacote e o endereço do cliente
    message, address = serverSocket.recvfrom(1024)
    
    print(message) # Mensagem recebida do dns_cliente

    serverSocket.sendto(message, address)