import cv2
import numpy as np

nameWindow="Calculadora"
def nothing(x):
    pass
def constructorVentana():
    cv2.namedWindow(nameWindow)
    cv2.createTrackbar("min",nameWindow,0,255,nothing)
    cv2.createTrackbar("max", nameWindow, 100, 255, nothing)
    cv2.createTrackbar("kernel", nameWindow, 1, 100, nothing)
    cv2.createTrackbar("areaMin", nameWindow, 500, 10000, nothing)

def calcularAreas(figuras):
    areas=[]
    for figuraActual in figuras:
        areas.append(cv2.contourArea(figuraActual))
    return areas

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
            if len(vertices) == 3:
                print("Triangulo")
                mensaje = "Triangulo"                
                cv2.drawContours(imagenOriginal, [figuraActual], 0, (0, 0, 255), 2)
                M=cv2.moments(figuraActual)
                if M['m00']!=0:
                    cx= int(M['m10']/M['m00'])
                    cy= int(M['m01']/M['m00'])
                    cv2.putText(imagenOriginal, mensaje, org=(cx,cy),fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),thickness=2, lineType=cv2.LINE_AA)
            elif len(vertices) == 4:
                print("Cadrado")
                mensaje = "Cuadrado"
                cv2.drawContours(imagenOriginal, [figuraActual], 0, (0, 0, 255), 2)
                M=cv2.moments(figuraActual)
                if M['m00']!=0:
                    cx= int(M['m10']/M['m00'])
                    cy= int(M['m01']/M['m00'])
                    cv2.putText(imagenOriginal, mensaje, org=(cx,cy),fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),thickness=2, lineType=cv2.LINE_AA)
            elif len(vertices) == 5:
                print("Pentagono")
                mensaje = "Pentagono"
                cv2.drawContours(imagenOriginal, [figuraActual], 0, (0, 0, 255), 2)
                M=cv2.moments(figuraActual)
                if M['m00']!=0:
                    cx= int(M['m10']/M['m00'])
                    cy= int(M['m01']/M['m00'])
                    cv2.putText(imagenOriginal, mensaje, org=(cx,cy),fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),thickness=2, lineType=cv2.LINE_AA)
        i = i + 1
    ##for (i,c) in enumerate(figuras):
    ##    M= cv2.moments(c)
    ##    if M['m00']!=0:
    ##        cx= int(M['m10']/M['m00'])
    ##        cy= int(M['m01']/M['m00'])
    ##        cv2.putText(imagenOriginal, text= str(i+1), org=(cx,cy),fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),thickness=2, lineType=cv2.LINE_AA)
    ##return imagenOriginal

video=cv2.VideoCapture(0)
constructorVentana()
while True:
    _,frame=video.read()
    detectarFigura(frame)
    cv2.imshow("Imagen",frame)


    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
video.release()
cv2.destroyAllWindows()