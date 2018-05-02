import numpy as np 
import cv2 as cv
import socket 
from matplotlib import pyplot as plt
import pickle
import itertools
import csv
import json

cap=cv.VideoCapture(0)


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1',9999))

rest, frame =cap.read()

print(frame)
pickle.dumps(frame)
plt.imshow(frame, interpolation='nearest')
plt.show()

while True:
   
    # c= str.encode(frame.encoding)
   
    ar = json.loads(frame)

    with open("output.csv", "wb") as f:
        writer = csv.writer(f)
        writer.writerows(ar)
    data = s.recv(1024)
    
    print ("Received", repr(data))
    if cv.waitKey(1) & 0xFF == ord ('q'): break
   
s.close()



#
# s.close()
# cap.release()
# cv.destroyAllWindows()
