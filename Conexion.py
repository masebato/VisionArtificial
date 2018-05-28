import io
import os
import random
import socket
# noinspection PyCompatibility
import struct
import subprocess
import cv2
import numpy as np

#from picamera import PiCamera
#from picamera.array import PiRGBArray
#instanciamos un objeto para trabajar con el socket

server_ip = '192.168.1.202'
if b"Fede Android" in subprocess.check_output("netsh wlan show interfaces"):
    server_ip = '192.168.1.202'
print("Inicializando stream...")
sock = socket.socket()

sock.bind(("",9999))
sock.listen(1)

sc, addr = sock.accept()
sc= sc.makefile('rb')
print("Connected by", addr)
while True:

    # Read the length of the image as a 32-bit unsigned int. If the
    # length is zero, quit the loop
    image_len = struct.unpack('<L', sc.read(struct.calcsize('<L')))[0]
    if not image_len:
        print('Finalizado por Cliente')
        break
    # Construct a stream to hold the image data and read the image
    # data from the connection
    image_stream = io.BytesIO()
    image_stream.write(sc.read(image_len))

    image_stream.seek(0)

    jpg = image_stream.read()
    roi = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)
    # region es Y, X        roi = roi[120:240, :]
    # mostrar la imagen
    cv2.imshow('Computer Vision', roi)

    # data = sc.recv(1024)

    # if not data: break
    # cv.imshow("RECIBIDO",data)
    # sc.sendall(data)
    
    # if cv.waitKey(1) & 0xFF == ord ('q'):break
        
    
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