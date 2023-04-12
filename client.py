
from socket import *

def clientTCP():
    serverName = '10.42.0.32'
    portNumber = 12300
    value = input('Enter a number between 1 and 100: ')
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, portNumber))

    try:
        name = 'Client of Misge Moges'
        data = f'{name},{value}'
        clientSocket.sendall(data.encode())
        data = clientSocket.recv(1024)
        data = data.decode()
        if data != '':
            server_name, serverValue = data.split(',')
        else:
            raise ValueError('Value out of range')
        result = int(value) + int(serverValue)
        print(f'{name} sent:  {value}')
        print(f'{server_name} sent: {serverValue}')
        print(f'Sum is: {result}')
        
    finally:
        clientSocket.close()
clientTCP()
