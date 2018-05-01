import numpy as np 
import cv2 as cv
import socket 
import time
#from picamera import PiCamera
#from picamera.array import PiRGBArray
#instanciamos un objeto para trabajar con el socket


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("",9999))

sock.listen(1)
sc, addr = sock.accept()
print("Connected by", addr)
while True:
    data = sc.recv(1024)

    if not data: break

    sc.sendall(data)
    
    if cv.waitKey(1) & 0xFF == ord ('q'):break
        
    print(data)
sc.close()

 
# while True:
   
#     #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro 
#     #la cantidad de bytes para recibir
   
   
#     recibido = sock.rec(1024)
#     # cv.imshow('Recibido', sc)
#     sock.send(recibido)
#     #Si el mensaje recibido es la palabra q se cierra la aplicacion
#     if cv.waitKey(1) & 0xFF == ord ('q'):
#         break
 
#     #Si se reciben datos nos muestra la IP y el mensaje recibido
#     print (" dice: ", recibido)
 
  
# print ("Adios.")
 
# #Cerramos la instancia del socket cliente y servidor
# sc.close()
# sock.close()