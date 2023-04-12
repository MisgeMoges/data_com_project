
from socket import*
def serverTCP():
    host = "localhost"
    portNumber = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind((host, portNumber))
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
            server_value = 45

            if int(value) < 1 or int(value) > 100:
                raise ValueError('Value out of range')
            result = int(value) + server_value
            clientSocket.sendall(f'{server_name},{server_value}'.encode())
            print(f'{name} sent {value}, server sent {server_value}, sum is {result}')

        except (ValueError, ConnectionResetError):
            # Handle out of range values and closed connections
            print(f'{name} disconnected')
            clientSocket.close()

serverTCP()