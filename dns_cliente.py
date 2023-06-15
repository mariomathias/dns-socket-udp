from socket import *

HOST = '127.0.0.1'
PORT = 50000

#Criando socket UDP
sock = socket(AF_INET, SOCK_DGRAM)

#Cliente escolhe um nome que esteja dentro da matriz de endereço
message = input("Digite um nome: ")

#Envia pro DNS
sock.sendto(message.encode(), (HOST, PORT))


#Recebe a resposta do DNS
response, addr = sock.recvfrom(1024)

sockServer = (response, 8000)

try:
    msg = input("Digite a mensagem: ")
    sock.sendto(msg.encode(), sockServer)
except:
    print("O nome não existe no DNS!")

print(response)