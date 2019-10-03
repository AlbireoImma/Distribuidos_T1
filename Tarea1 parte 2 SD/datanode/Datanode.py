import socket, time
from threading import Thread

SERVER = "localhost"
PORT = 5000

def HeartBeat(datanode):
    """
    Funcion la cual envia un mensaje periodicamente al server para identificar su funcionamiento
    """
    while True:
        time.sleep(4)
        datanode.sendall(bytes("Alive", 'UTF-8'))

datanode = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
datanode.connect((SERVER,PORT))
entrada = datanode.recv(1024)
print("[Headnode]", entrada.decode())
datanode.sendall(bytes("Datanode", 'UTF-8'))

Thread(target=HeartBeat,args=[datanode]).start()

while True:
    datos = datanode.recv(2048)
    entrada = datos.decode()
    datafile = open("data.txt","a+")
    datafile.write(entrada+"\n")
    datafile.close()

datanode.close()