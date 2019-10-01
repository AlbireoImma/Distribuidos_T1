import socket


flag = True
puerto = 5000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(("server",puerto))
print("Conectando al servidor\n")



respuesta = open('respuestas.txt','w')
respuesta.close()

try: 
	respuesta = open('respuestas.txt','a')


	msj = "Hola servidor"
	sock.sendall(bytes(msj,'utf-8'))
	respuesta.write("Saludando al servidor\n")

	mensaje = sock.recv(1024)
	print("Servidor: "+mensaje.decode("utf-8")+'\n')
	respuesta.write("Servidor: "+mensaje.decode('utf-8')+'\n')

	msj = 'quit'
	sock.sendall(bytes(msj,'utf-8'))
	mensaje = sock.recv(1024)
	print("Servidor: " +mensaje.decode("utf-8")+'\n')

finally:
	
	respuesta.write("Desconectandose del servidor\n")
	respuesta.close()
	sock.close()
