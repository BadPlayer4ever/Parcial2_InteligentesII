import cv2
import numpy as np
import keyboard
import os

nameWindow="Calculadora"
def nothing(x):
    pass
def constructorVentana():
    cv2.namedWindow(nameWindow)
    cv2.createTrackbar("min",nameWindow,0,255,nothing)
    cv2.createTrackbar("max", nameWindow, 100, 255, nothing)
    cv2.createTrackbar("kernel", nameWindow, 5, 100, nothing)
    cv2.createTrackbar("areaMin", nameWindow, 2000, 10000, nothing)

def calcularAreas(figuras):
    areas=[]
    for figuraActual in figuras:
        areas.append(cv2.contourArea(figuraActual))
    return areas

def capturarRecortes(imagenOriginal):
    imagenGris=cv2.cvtColor(imagenOriginal,cv2.COLOR_BGR2GRAY)
    min = cv2.getTrackbarPos("min", nameWindow)
    max = cv2.getTrackbarPos("max", nameWindow)
    bordes = cv2.Canny(imagenGris, min, max)
    tamañoKernel = cv2.getTrackbarPos("kernel", nameWindow)
    kernel = np.ones((tamañoKernel, tamañoKernel), np.uint8)
    bordes = cv2.dilate(bordes, kernel)
    figuras, jerarquia = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = calcularAreas(figuras)
    i = 0
    areaMin = cv2.getTrackbarPos("areaMin", nameWindow)
    c=0
    filelist = [ f for f in os.listdir("capturas") if f.endswith(".png") ]
    for f in filelist:
        os.remove(os.path.join("capturas", f))
    
    for figuraActual in figuras:        
        if areas[i] >= areaMin:
            # Coordenadas vértices
            vertices = cv2.approxPolyDP(figuraActual, 0.05 * cv2.arcLength(figuraActual, True), True)
            if len(vertices) == 4:                
                
                # Recorte de imagen

                contour_image = np.zeros_like(imagenOriginal)

                cv2.drawContours(contour_image, [figuraActual], -1, (255, 255, 255), cv2.FILLED) # Contorno en blanco
                
                x, y, w, h = cv2.boundingRect(figuraActual)
                cropp = imagenOriginal[y:y+h, x:x+w]

                cropp= cv2.resize(cropp,[128,128], interpolation= cv2.INTER_AREA)   

                

                cv2.imwrite(f"capturas/contorno_{i}.png", cropp)
        i = i + 1

def detectarFigura(imagenOriginal):
    imagenGris=cv2.cvtColor(imagenOriginal,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gris", imagenGris)    
    min = cv2.getTrackbarPos("min", nameWindow)
    max = cv2.getTrackbarPos("max", nameWindow)
    bordes = cv2.Canny(imagenGris, min, max)
    tamañoKernel = cv2.getTrackbarPos("kernel", nameWindow)
    kernel = np.ones((tamañoKernel, tamañoKernel), np.uint8)
    bordes = cv2.dilate(bordes, kernel)
    figuras, jerarquia = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = calcularAreas(figuras)
    i = 0
    areaMin = cv2.getTrackbarPos("areaMin", nameWindow)
    c=0
    for figuraActual in figuras:        
        if areas[i] >= areaMin:
            # Coordenadas vértices
            vertices = cv2.approxPolyDP(figuraActual, 0.05 * cv2.arcLength(figuraActual, True), True)
            if len(vertices) >= 4:
                mensaje = "Dado"             
                cv2.drawContours(imagenOriginal, [figuraActual], 0, (0, 0, 255), 2)
                M=cv2.moments(figuraActual)
                if M['m00']!=0:
                    cx= int(M['m10']/M['m00'])
                    cy= int(M['m01']/M['m00'])
                    cv2.putText(imagenOriginal, mensaje, org=(cx,cy),fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255,0,0),thickness=2, lineType=cv2.LINE_AA)
                
        i = i + 1

video=cv2.VideoCapture(0)
constructorVentana()
while True:
    _,frame=video.read()
    if keyboard.is_pressed("p"):
        pressed=True
        print ("Captura")
        capturarRecortes(frame)
        while pressed:
            if not keyboard.is_pressed("p") :
                pressed =False
    detectarFigura(frame)
    cv2.imshow("Imagen",frame)

    


    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
video.release()
cv2.destroyAllWindows()