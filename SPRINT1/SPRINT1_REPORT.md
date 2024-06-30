# Sprint 1: Configuración del entorno y adquisición de datos
# 1) INTRODUCCIÓN:
# Objetivos:
• Configurar el entorno de desarrollo con las bibliotecas necesarias.

• Recopilar y preprocesar un conjunto de datos de imágenes.

• Implementar una red neuronal simple para la detección de objetos en un entorno local.

Los objetivos del sprint 1 son necesarios, pues es necesario configurar el entorno de desarrollo con las bibliotecas necesarias para su posterior uso. Además, se va a tener que recopilar y preprocesar el conjunto de datos de imágenes. Finalmente, definir la arquitectura de la red neuronal para entrenarla con los datos preprocesados.

================
# 2) PLANIFICACIÓN:
# *Tareas planificadas:*

## • **Tarea 1: Configurar el entorno de desarrollo**

Para el sprint 1, se implementaron las siguientes librerías:
- Numpy: Manejo de datos
- xml: Leer los archivos xml
- os: Obtener las rutas de los archivos
- PIL: Manipulación de imágenes
- Tensorflow & Keras: Creación de redes neuronales

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/lib.PNG)

## • **Tarea 2: Recopilar y preprocesar un conjunto de datos de imágenes**

### **- RECOPILACIÓN DE IMÁGENES**

El conjunto de imágenes fue dividido en datos de *training* y *testing*:

* Datos de *training*:
  Consta de 1400 archivos. Cada imagen tiene su archivo 'xml' correspondiente, los cuales contienen la clase del objeto que está en la imagen, así como el 
  *bounding box*. Es decir, el archivo 'xml' es el archivo que contiene toda la información de la imagen ya etiquetada.
  La data de training consta de 700 imágenes.
  
* Datos de *testing*:
  Consta de 194 archivos (imágenes + xml) para evaluar el *performance* de la red neuronal luego de su entrenamiento. 

### **- PREPROCESAMIENTO DEL CONJUNTO DE IMÁGENES**
Para el preprocesamiento de imágenes, primero fue necesario tener las imágenes como matrices, para lo cual se usaron las librerías 'os' y 'PIL'.

**OS**: Debido a que las imágenes estaban contenidas en un directorio, se usó esta librería para obtener las rutas, tanto de las imágenes como de los archivos xml.

**PIL**: Se usó esta librería para leer la ruta de la imagen y obtenerla en una matriz.

Los pasos anteriores fueron realizados mediante dos funciones:

**-** Se implementaron dos funciones en el sprint 1 para la recopilación y el procesamiento de imágenes:

**--** La función "Imagenes" se encarga de leer la ruta de la imagen, el resize y la conversión a un arreglo de Numpy.
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/imge.PNG)

**--** La función "Data" se encarga de leer cada uno de los archivos xml que contienen los bounding boxes y clases de las imágenes etiquetadas. Asimismo, dentro de dicha función, se encuentra "Imagenes" para leerlo y realizar el procesamiento de las imágenes directamente.
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/data1.PNG)

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/data2.PNG)

El preprocesamiento de las imágenes, como la normalización de las mismas (colocar cada píxel de la imagen en un rango de 0 a 1) se hace en la red neuronal. Es decir, la primera 'capa' de la red se encargará de realizar la normalización:
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/Rescaling.PNG)

## • **Tarea 3: Implementar una red neuronal simple para la detección de objetos en un entorno local**
ARQUITECTURA DE LA RED NEURONAL:
-Capas de convolución: 5 capas de convolución con un kernel de 3. A cada capa se le aplica el padding, de tal forma que cuando se apliquen cada uno de los filtros a las imágenes, la matriz resultante no se reduzca en forma, es decir, tenga el mismo shape que la matriz de entrada

-Capas de MaxPooling: Luego de cada capa de convolución, se le aplica la capa de MaxPooling --> 5 capas de MaxPooling. Las capas de MaxPooling se encargarán de extraer los píxeles con 'mayor relevancia' (píxeles de mayor valor en la matriz de salida) luego de haber aplicado los filtros a cada una de las imágenes en las capas de convolución; de esta forma, la matriz se hace más pequeña y, por lo tanto, más eficiente serán las operaciones para las próximas capas, puesto que el shape de la matriz de entrada se va reduciendo.

-Capas de BatchNormalization: 4 capas de BatchNormalization. Las capas de 'normalización' (batch normalization) se encargarán de 'centrar' y 'normalizar' cada mini-batch que llega a la red, añadiendo el hecho de que también introduce cierto ruido que actúa como regularización y así prevenir el overfitting.

-Capas lineales:

2 capas densas (lineales) para la clasificación.
4 capas densas (lineales) para la regresión.

**Red neuronal**:
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/rn.PNG)

==========
# Tiempo que tomó el entrenamiento
Las GPU están diseñadas con una gran cantidad de núcleos que pueden realizar múltiples operaciones simultáneamente.
Las GPU tienen miles de núcleos más pequeños y eficientes diseñados para tareas paralelas. Esta arquitectura permite a las GPU manejar las operaciones matriciales y vectoriales que son fundamentales para el entrenamiento de redes neuronales de manera mucho más eficiente.
Sin embargo, en el primer sprint no se usó GPU aún, por lo que el tiempo (entrenando al modelo con solo 10 épocas) fue de 1225.860 seg. (20 min.) aproximadamente:
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/tiempo.PNG)
