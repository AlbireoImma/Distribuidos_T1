import socket
import threading
import sys

def thread_recibe(conexion,ip,archivo):

	
	mensaje = conexion.recv(1024)
	arc = open(archivo,'a')
	arc.write('Mensaje de '+str(ip[0])+':'+str(ip[1])+'   '+mensaje.decode("utf-8")+'\n')
	arc.close()
	conexion.sendall(bytes('Hola Cliente!','utf-8'))
	while True:
		try:
			mensaje = conexion.recv(1024)
			if mensaje.decode("utf-8") == 'quit':
				arc = open(archivo,'a')
				arc.write('El cliente '+str(ip[0])+ ':' +str(ip[1])+ ' se ha desconectado\n')
				arc.close()
				conexion.sendall(bytes('Te has desconectado','utf-8'))	

		except:
			conexion.close()
			sys.exit()


puerto = 5000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("server",puerto))
sock.listen(1)     
log = open('log.txt','w')
log.close()

while True:
	nombre = 'log.txt'
	log = open('log.txt','a')


	conexion,ipcl = sock.accept()

	log.write('Conexion aceptada del cliente: '+str(ipcl[0])+':'+str(ipcl[1])+'\n')
	log.close()
	recibe = threading.Thread(target=thread_recibe, args= (conexion,ipcl,nombre))
	recibe.start()
