# Parcial2_InteligentesII

Estudiante: Camilo Vargas  -  Daniel Fernando Sanchez

NOTA: Se resubio copia del video debido a audio corrupto. Se recomienda escuchar el video con todo el volumen

Estructura del proyecto:
-Carpeta DataSet: El dataset se encuentra dentro de la carpeta DataSet, dentro se encuentran carpetas con imagenes enumeradas correspondientes a cada una de las categorias. Cada categoria cuenta con 20 fotos, para un total de 120 muestras

-Carpeta Predicciones: se encuentra el archivo entrenamiento.py, que fue el archivo usado para entrenar y guardar los 3 modelos de aprendizaje. Tambien se encuentra el archivo PruebasPrediccion.py Que fue el usado para realizar las pruebas tiempo de los modelos.

-Carpeta Capturas: Se encuentran las capturas de los contornos  

-Carpeta Models: Aqui se guardan los archivos h5 de los modelos

-El archivo ShapeDetection es una demostracion de la captura de imagenes geometricas a traves de OpenCV

-El archivo ShapeCropping es una demostracion de la captura y recorte de los contornos geometricos detectados por OpenCV

-El archivo parcial2.py es la aplicacion final de captura y prediccion de dados por camara. Para tomar captura de los dados y sumarlos basta con presionar la tecla P

Pruebas:

Las pruebas se realizaron a los tres modelos de aprendizaje implementados, cambiando las epocas de aprendizaje y el numero de batch

| Nombre  | Accuracy               | Precision              | Recall                 | F1 Score               | loss                   | Epochs | Tiempo de respuesta (2 detecciones) |
|---------|------------------------|------------------------|------------------------|------------------------|------------------------|--------|-----------------------------------|
| ModeloA | 0.8666666746139526     | 0.9230769276618958     | 0.800000011920929      | 0.6933333553314208     | 0.4817933142185211     | 10     | 0.6131973266601562               |
| ModeloB | 0.9688                 | 0.9791                 | 0.947                  | 0.9662                 | 0.18007                | 30     | 0.41141271591186523              |
| ModeloC | 0.9791666865348816     | 0.988723406791687      | 0.9583333134651184     | 0.9784210437288574     | 0.17321038246154785    | 20     | 0.5040385723114014               |
