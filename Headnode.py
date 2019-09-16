import socket, threading

class HiloCliente(threading.Thread):
    """
    Clase con la lógica del servidor, necesita la IP y Socket del cliente\n
    Retorna un hilo, el cual puede ser ejecutado con hilo.start() y ejecuta el método run() de la clase
    """
    def __init__(self,IP_Cliente,Socket_Cliente):
        threading.Thread.__init__(self)
        self.SocketCliente = Socket_Cliente
        print("Nueva conexión: ", IP_Cliente)
    def run(self):
        print("Conexión desde : ", IP_Cliente)
        self.SocketCliente.send(bytes("Hola, este es el servidor", 'utf-8'))
        entrada = ''
        while True:
            datos = self.SocketCliente.recv(2048)
            entrada = datos.decode()
            if entrada == 'bye':
                break
            print("Mensaje desde el cliente :", entrada)
            self.SocketCliente.send(bytes(entrada,'UTF-8'))
        print("Cliente en ", IP_Cliente , "desconectado")

LOCALHOST = "127.0.0.1"
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST,PORT))
print("Servidor iniciado")
print("Esperando peticiones de clientes...")
while True:
    server.listen(1)
    Socket_Cliente, IP_Cliente = server.accept()
    hilo = HiloCliente(IP_Cliente,Socket_Cliente)
    hilo.start()