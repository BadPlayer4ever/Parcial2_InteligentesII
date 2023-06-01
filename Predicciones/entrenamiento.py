import tensorflow as tf
import keras
import keras_metrics
import numpy as np
import cv2
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import InputLayer,Input,Conv2D, MaxPool2D,Reshape,Dense,Flatten

def cargarDatos(rutaOrigen,numeroCategorias,limite,ancho,alto):
    imagenesCargadas=[]
    valorEsperado=[]
    for categoria in range(0,numeroCategorias):
        for idImagen in range(0,limite[categoria]):
            ruta=rutaOrigen+str(categoria+1)+"/"+str(categoria+1)+"_"+str(idImagen)+".png"
            print(ruta)
            imagen = cv2.imread(ruta)
            imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            imagen = cv2.resize(imagen, (ancho, alto))
            imagen = imagen.flatten()
            imagen = imagen / 255
            imagenesCargadas.append(imagen)
            probabilidades = np.zeros(numeroCategorias)
            probabilidades[categoria] = 1
            valorEsperado.append(probabilidades)
    imagenesEntrenamiento = np.array(imagenesCargadas)
    valoresEsperados = np.array(valorEsperado)
    return imagenesEntrenamiento, valoresEsperados

#################################
ancho=128
alto=128
pixeles=ancho*alto
#Imagen RGB -->3
numeroCanales=1
formaImagen=(ancho,alto,numeroCanales)
numeroCategorias=6

cantidaDatosEntrenamiento=[16,16,16,16,16,16]
cantidaDatosPruebas=[8,8,8,8,8,8]

#Cargar las imágenes
imagenes, probabilidades=cargarDatos("dataset/train/",numeroCategorias,cantidaDatosEntrenamiento,ancho,alto)
imagenesPrueba, probabilidadesPrueba=cargarDatos("dataset/test/",numeroCategorias,cantidaDatosPruebas,ancho,alto)

model=Sequential()
#Capa entrada
model.add(InputLayer(input_shape=(pixeles,)))
model.add(Reshape(formaImagen))

#Capas Ocultas
#Capas convolucionales
model.add(Conv2D(kernel_size=5,strides=2,filters=16,padding="same",activation="relu",name="capa_1"))
model.add(MaxPool2D(pool_size=2,strides=2))

model.add(Conv2D(kernel_size=3,strides=1,filters=36,padding="same",activation="relu",name="capa_2"))
model.add(MaxPool2D(pool_size=2,strides=2))

#Aplanamiento
model.add(Flatten())
model.add(Dense(128,activation="relu"))

#Capa de salida
model.add(Dense(numeroCategorias,activation="softmax"))


#Traducir de keras a tensorflow
model.compile(optimizer="adam",loss="categorical_crossentropy", metrics=["accuracy",tf.keras.metrics.Precision(), tf.keras.metrics.Recall()])
#Entrenamiento
model.fit(x=imagenes,y=probabilidades,epochs=20,batch_size=32)


#Prueba del modelo

imagenesPrueba,probabilidadesPrueba=cargarDatos("dataset/test/",numeroCategorias,cantidaDatosPruebas,ancho,alto)
resultados=model.evaluate(x=imagenesPrueba,y=probabilidadesPrueba,verbose=0)
loss= resultados[0]
accuracy = resultados[1]
precision = resultados [2]
recall = resultados [3]
f1Score = 2 * ( (precision * recall) / (precision + recall))

print("###### RESULTADOS ######")
print("Loss= "+str(loss))
print("Accuracy= "+str(accuracy))
print("Precision= "+str(precision))
print("Recall= "+str(recall))
print("f1Score= "+str(f1Score))


# Guardar modelo
ruta="models/modeloC.h5"
model.save(ruta)
# Informe de estructura de la red
model.summary()
