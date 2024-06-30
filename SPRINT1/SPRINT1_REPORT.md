# Sprint 1: Configuración del entorno y adquisición de datos
# Objetivos:
• Configurar el entorno de desarrollo con las bibliotecas necesarias.

• Recopilar y preprocesar un conjunto de datos de imágenes.

• Implementar una red neuronal simple para la detección de objetos en un entorno local.

================

• *Entorno de desarrollo*

Se implementaron las siguientes librerías:
- Numpy: Manejo de datos
- xml: Leer los archivos xml
- os: Obtener las rutas de los archivos
- PIL: Manipulación de imágenes
- Tensorflow & Keras: Creación de redes neuronales

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/lib.PNG)

• *Recopilar y preprocesar un conjunto de imágenes de datos de imágenes*

- Se implementaron dos funciones en el sprint 1 para la recopilación y el procesamiento de imágenes:

-- La función "Imagenes" se encarga de leer la ruta de la imagen, el resize y la conversión a un arreglo de Numpy.
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/imge.PNG)

-- La función "Data" se encarga de leer cada uno de los archivos xml que contienen los bounding boxes y clases de las imágenes etiquetadas. Asimismo, dentro de dicha función, se encuentra "Imagenes" para leerlo y realizar el procesamiento de las imágenes directamente.
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/data1.PNG)

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/data2.PNG)

• *Implementar una red neuronal simple para la detección de objetos en un entorno local*

Red neuronal:
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/rn.PNG)
