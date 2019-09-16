import socket

SERVER = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((SERVER,PORT))
cliente.sendall(bytes("Este es el cliente", 'UTF-8'))

while True:
    entrada = cliente.recv(1024)
    print("Desde el servidor :", entrada.decode())
    salida = input()
    cliente.sendall(bytes(salida, 'UTF-8'))
    if salida == 'bye':
        break
cliente.close()