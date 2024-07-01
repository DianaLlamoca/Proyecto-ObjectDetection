# SRINT 2: ESCALABILIDAD Y PARALELIZACIÓN
# 1) INTRODUCCIÓN:
# Objetivos:
• Distribuir el procesamiento de imágenes utilizando técnicas de paralelismo.

• Implementar una cola de tareas para gestionar el procesamiento de imágenes.

• Optimizar la red neuronal para ejecución distribuida

En el sprint 2 se intentará mejorar el tiempo de entrenamiento respecto al sprint 1 usando GPU. Así, se aprovechará dicho recurso para acelerar la etapa de training. Además, se usó "concurrent.futures" para leer las rutas de las imágenes y sus archivos xml correspondientes.
De forma general, se aprovecharán las técnicas de paralelismo, tanto para el procesamiento de las imágenes, como para el entrenamiento de la red neuronal.

=========

# 2) PLANIFICACIÓN:
# Tareas planificadas:
## * Tarea 1: Distribuir el procesamiento de imágenes utilizando técnicas de paralelismo
  Para el sprint 2, se implementó la librería "concurrent.futures": Se implementaron técnicas de paralelismo, usando un pool de procesos, haciendo uso de 
  "concurrent.futures", con el objetivo de que cada proceso del pool se encargue de ejecutar la tarea de leer la imagen desde la ruta, obtener los datos más 
  importantes de los archivos 'xml' para obtener los bounding boxes y la clase correspondiente, hasta el resize de cada imagen de la data:

  ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/CF.PNG)
  
  ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/cfu.PNG)

  En las funciones encargadas para realizar el procesamiento de las imágenes (funciones "Imagenes" y "Data" del primer sprint") se aplicó el paralelismo para 
  distribuir el procesamiento de imágenes a cada proceso.

  * **Pool de procesos para la data de *train***: Se creó un Pool de procesos usando la librería "concurrent.futures", de tal forma que a cada proceso se le asigna 
    una ruta para que la lea y se haga el procesamiento:
    ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/p1.PNG)

  * **Pool de procesos para la data de *test***: Se creó un Pool de procesos usando la librería "concurrent.futures", de tal forma que a cada proceso se le asigna 
    una ruta para que la lea y se haga el procesamiento:
    ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/p_.PNG)
    
  
  
## * Tarea 2: Uso de GPU para mejora del tiempo en el entrenamiento de la red neuronal:
  ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU1.PNG)

## 1) Sistema de procesamiento de imágenes distribuido utilizando concurrent.futures:
En el sprint 2, se implementó técnicas de paralelismo, usando un pool de procesos, haciendo uso de "concurrent.futures", con el objetivo de que cada proceso del pool se encargue de ejecutar la tarea de leer la imagen desde la ruta, obtener los datos más importantes de los archivos 'xml' para obtener los bounding boxes y la clase correspondiente, hasta el resize de cada imagen de la data:

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/CF.PNG)

## 2) Red neuronal optimizada para ejecución distribuida:
Acá se ajustó la arquitectura de la red neuronal para mejorar el rendimiento en un entorno distribuido, teniendo en cuenta el número de GPU's disponibles.
Se usó "*tf.distribute.Strategy*", el cual proporciona una abstracción para realizar la ejecución distribuida en varias unidades de procesamiento.
Esta estrategia funciona de la siguiente manera: Esencialmente, se copia todas las variables del modelo a cada GPU. Luego, se usa "all-reduce" para combinar los gradientes de todos los GPU y aplica el valor combinado a todas las copias del modelo.

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU1.PNG)

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU2.PNG)

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU3.PNG)

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU4.PNG)
