import socket

SERVER = "0.0.0.0"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((SERVER,PORT))
entrada = cliente.recv(1024)
print("[Headnode]", entrada.decode())
cliente.sendall(bytes("Cliente", 'UTF-8'))

def registrar(entrada):
    """
    Funcion para registrar donde se guardo el dato enviado al headnode\n
    La entrada corresponde al mensaje del server
    """
    registro = open("Registro_Cliente.txt","a+")
    registro.write(entrada + "\n")
    registro.close()

while True:
    print("Ingrese su dato [escriba salir para terminar rutina]")
    salida = input()
    if salida == 'salir':
        break
    else:
        cliente.sendall(bytes(salida, 'UTF-8'))
        entrada = cliente.recv(1024).decode()
        print("[Headnode]", entrada)
        registrar(entrada)
cliente.sendall(bytes(salida, 'UTF-8'))
cliente.close()