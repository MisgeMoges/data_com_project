
from socket import *
def clientTCP():
    serverName = 'localhost'
    portNumber = 12000
    value = input('Enter a number between 1 and 100: ')
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, portNumber))

    try:
        name = 'Client of Misge Moges'
        data = f'{name},{value}'
        clientSocket.sendall(data.encode())
        data = clientSocket.recv(1024)
        server_name, serverValue = data.decode().split(',')
        result = int(value) + int(serverValue)
        print(f'{server_name} sent {serverValue}, {name} sent {value}, sum is {result}')

    finally:
        clientSocket.close()
clientTCP()
