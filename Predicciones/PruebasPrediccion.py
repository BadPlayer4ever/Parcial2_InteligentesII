
import cv2
from Prediccion import Prediccion
import time

clases=[1,2,3,4,5,6]

ancho=128
alto=128

miModeloCNN=Prediccion("models/modeloC.h5",ancho,alto)
imagen1=cv2.imread("dataset/prueba.png")
imagen2=cv2.imread("dataset/prueba2.png")

start = time.time()
claseResultado=miModeloCNN.predecir(imagen1)
claseResultado2=miModeloCNN.predecir(imagen2)
end = time.time()

dado1= clases[claseResultado]
dado2 = clases[claseResultado2]
print("Dado 1: " + str(clases[claseResultado]))
print("Dado 2: " + str(clases[claseResultado2]))
print("Tiempo: "+ str(end-start))
print ("suma de los dados: "+str(dado1+dado2))

while True:
    cv2.imshow("imagen1",imagen1)
    cv2.imshow("imagen2",imagen2)
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cv2.destroyAllWindows()