
from socket import*
import random
def serverTCP():
    portNumber = 12300
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('', portNumber))
    serverSocket.listen(1)

    while True:
        server_name = 'Server of Misge Moges'
        print(f' {server_name} is ready to listen...')
        clientSocket, client_address = serverSocket.accept()
        print(f'{server_name} connected with {client_address}')

        try:
            data = clientSocket.recv(1024)
            name, value = data.decode().split(',')
            print(f'{name} connected with {server_name} ')
            server_value = random.randint(1, 100)

            if int(value) < 1 or int(value) > 100:
                raise ValueError('Value out of range')
            result = int(value) + server_value
            clientSocket.sendall(f'{server_name},{server_value}'.encode())
            print(f'{name} sent:  {value}')
            print(f'{server_name} sent: {server_value}')
            print(f'Sum is: {result}')
           
        except (ValueError, ConnectionResetError):
            print(f'{name} disconnected')
            clientSocket.close()

serverTCP()