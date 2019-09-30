import socket, threading, time
from datetime import datetime
import random

DATANODES = []

def registrar(entrada):
    registro = open("Registro_Server.txt","a+")
    registro.write(entrada + "\n")
    registro.close()

def Rutina_Cliente(SocketCliente,IP_Cliente):
    """
    Funcion que contiene la logica del funcionamiento del servidor para los clientes\n
    Envia los mensajes hacia los datanodes y mantiene el registro del servidor en Registro_Server.txt ademas de log.txt
    """
    host, port = SocketCliente.getpeername()
    log = open("log.txt","a+")
    log.write("[Conexión] Cliente " + str(host) + " : " + str(port)+ "\n")
    log.close()
    while True:
        datos = SocketCliente.recv(2048)
        entrada = datos.decode()
        if entrada == 'salir':
            break
        # print("[Cliente]", entrada)
        datanode = random.choice(DATANODES)
        datanode.sendall(datos)
        pair = datanode.getpeername()
        msg = str(pair[0]) + ":" + str(pair[1])
        registrar(msg)
        SocketCliente.send(bytes(msg,'UTF-8'))
    log = open("log.txt","a+")
    log.write("[Desconexión] Cliente " + str(host) + " : " + str(port)+ "\n")
    log.close()
    print("Cliente en", IP_Cliente, "desconectado")

def Rutina_Datanode(SocketCliente,index):
    """
    Funcion que contiene la logica del funcionamiento del servidor para los datanodes\n
    Comprueba su disponibilidad y escribe su estado en el Hearbeat_Server.txt ademas de log.txt
    """
    host, port = Socket_Cliente.getpeername()
    log = open("log.txt","a+")
    log.write("[Conexión] Datanode " + str(host) + " : " + str(port)+ "\n")
    log.close()
    Health = True
    # print("HeartBeat:", Health)
    while Health:
        time.sleep(5)
        Health = Check_Datanode(SocketCliente)
        # print("HeartBeat:", Health)
        if Health:
            ts = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            heartbeat = open("Heartbeat_Server.txt","a+")
            heartbeat.write("[" + ts + "] Alive " + str(port) + "\n")
            heartbeat.close()
        else:
            ts = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            heartbeat = open("Heartbeat_Server.txt","a+")
            heartbeat.write("[" + ts + "] Dead " + str(port) + "\n")
            heartbeat.close()
    DATANODES.remove(SocketCliente)
    SocketCliente.close()
    log = open("log.txt","a+")
    log.write("[Desconexión] Datanode " + str(host) + " : " + str(port)+ "\n")
    log.close()


def Check_Datanode(SocketCliente):
    """
    Funcion la cual verifica la disponibilidad del datanode\n
    Hace uso del mensaje enviado por HeartBeat en Datanode.py
    """
    databack = SocketCliente.recv(2048)
    if databack:
        return True
    else:
        return False



class HiloCliente(threading.Thread):
    """
    Clase con la lógica del servidor, necesita la IP y Socket del cliente\n
    Retorna un hilo, el cual puede ser ejecutado con hilo.start() y ejecuta el método run() de la clase
    """
    def __init__(self,IP_Cliente,Socket_Cliente):
        threading.Thread.__init__(self)
        self.SocketCliente = Socket_Cliente
        print("Nueva conexión :", IP_Cliente)

    def run(self):
        """
        Funcion que se ejecuta al hacer HiloCliente().start\n
        Discrimina que rutina se ejecuta segun el mensaje que envia el socket si cliente o datanode
        """
        self.SocketCliente.send(bytes("Hola, este es el servidor", 'utf-8'))
        datos = self.SocketCliente.recv(2048)
        entrada = datos.decode()
        if entrada == "Cliente":
            Rutina_Cliente(self.SocketCliente,IP_Cliente)
        elif entrada == "Datanode":
            DATANODES.append(self.SocketCliente)
            Rutina_Datanode(self.SocketCliente,len(DATANODES))

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