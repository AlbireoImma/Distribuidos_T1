# Distribuidos_T1
Tarea #1 Sistemas Distribuidos - 2019-I

Para ejecutar el docker primero debemos construirlo:

> docker-compose build

Para iniciar el servicio del servidor hacemos:

> docker-compose run headnode

Para iniciar un datanode hacemos:

> docker-compose run datanode

Para iniciar el cliente hacemos:

> docker-compose run cliente

- Si los comandos no funcionan, el problema puede ser de permisos, usar sudo o su segun corresponda
- El funcionamiento debe seguir el orden (headnode -> datanode [las veces necesarias] -> cliente) ya que los sockets de cada servicio utilizan el de los anteriores ()
- Se puede llamar el servicio datanode mas de una vez
- El directorio de los archivos del server esta en ./headnode
- El directorio de los archivos del cliente esta en ./cliente
- El directorio de los archivos de los datanodes esta en ./datanode
- Podemos usar docker-compose up, pero nos falta una shell interactiva con la cual el cliente envie mensajes por lo cual es mas simple levantar los servicios uno a uno (la cantidad de datanodes los informamos de la opcion --scale datanodes=3)
