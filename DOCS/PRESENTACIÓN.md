# INTRODUCCIÓN: Comienza con una introducción que resuma el proyecto, sus objetivos y su relevancia
## - RESUMEN DEL PROYECTO:
El proyecto consiste en desarrollar un sistema distribuido de visión computacional para detectar objetos en imágenes. EL modelo de red neuronal debe realizar el problema de clasificación para detectar las clases en la imagen dada; asimismo, calculará las coordenadas de los bounding boxes que indican en dónde se encuentra el objeto. Además, para optimizar la escalabilidad y mejorar la eficiencia del entrenamiento de la red neuronal, se hará uso de la computación paralela y distribuida. De esta forma, cada 'nodo' se encargará de realizar un determinado trabajo, en paralelo con el resto, para optimizar el funcionamiento general del sistema.

## - OBJETIVOS:
### SPRINT 1:
• Configurar el entorno de desarrollo con las bibliotecas necesarias.

• Recopilar y preprocesar un conjunto de datos de imágenes.

• Implementar una red neuronal simple para la detección de objetos en un entorno local.

### SPRINT 2:
• Distribuir el procesamiento de imágenes utilizando técnicas de paralelismo.

• Implementar una cola de tareas para gestionar el procesamiento de imágenes.

• Optimizar la red neuronal para ejecución distribuida


## - RELEVANCIA:
La relevancia radica en el uso de técnicas de paralelismo empleadas y GPU. Estas aceleran y hacen más eficiente el entrenamiento de la red, así como el procesamiento de las imágenes al realizarse las tareas de forma paralela. Lo cual lleva a una reducción del tiempo empleado para una mejora incremental del desarrollo y entrenamiento de la red neuronal

=======

# Metodología: Explica brevemente la metodología utilizada, incluyendo el enfoque ágil y la estructura de los sprints.
- Metodología ágil: La metodología ágil permitió el desarrollo incremental en cada sprint, lo cual impactó en la reducción del tiempo de entrenamiento de la red neuronal al implementar técnicas de paralelismo.
- Estructura de los sprints:
  - Sprint 1:
    - Tareas planificadas:
    - Tarea 1: Configurar el entorno de desarrollo
    - Tarea 2: Recopilar y preprocesar un conjunto de datos de imágenes:
       - Recopilación de imágenes
       - Preprocesamiento del conjunto de imágenes
    - Tarea 3: Implementar una red neuronal simple para la detección de objetos en un entorno local:
       - Creación de la arquitectura de la red neuronal
  - Sprint 2:
     - Tareas planificadas:
       - Tarea 1: Distribuir el procesamiento de imágenes utilizando técnicas de paralelismo:
          - Pool de procesos para la data de train y test
       - Tarea 2: Uso de GPU para mejora del tiempo en el entrenamiento de la red neuronal
       - Tarea 3: Cuantización post-entrenamiento de la red
       
=======

## Desarrollo del proyecto: Desglosa el desarrollo del proyecto por sprints, destacando los objetivos y logros de cada sprint.
- Sprint 1:
    - Tareas planificadas:
    - Tarea 1: Configurar el entorno de desarrollo
      Para el sprint 1, se implementaron las siguientes librerías:
       - Numpy: Manejo de datos
       - xml: Leer los archivos xml
       - os: Obtener las rutas de los archivos
       - PIL: Manipulación de imágenes
       - Tensorflow & Keras: Creación de redes neuronales

       ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/lib.PNG)


    - Tarea 2: Recopilar y preprocesar un conjunto de datos de imágenes:
       - **Recopilación de imágenes:**
         - El conjunto de imágenes fue dividido en datos de *training* y *testing*:
           - Datos de *training*: Consta de 1400 archivos. Cada imagen tiene su archivo 'xml' correspondiente, los cuales contienen la clase del objeto que está en la imagen, así como el *bounding box*. Es decir, el archivo 'xml' es el archivo que contiene toda la información de la imagen ya etiquetada. La data de training consta de 700 imágenes.
  
           - Datos de *testing*: Consta de 194 archivos (imágenes + xml) para evaluar el *performance* de la red neuronal luego de su entrenamiento.
         
       - **Preprocesamiento del conjunto de imágenes:**
         - Para el preprocesamiento de imágenes, primero fue necesario tener las imágenes como matrices, para lo cual se usaron las librerías 'os' y 'PIL'.
         - **OS**: Debido a que las imágenes estaban contenidas en un directorio, se usó esta librería para obtener las rutas, tanto de las imágenes como de los archivos xml.
         - **PIL**: Se usó esta librería para leer la ruta de la imagen y obtenerla en una matriz.
       
         - Los pasos anteriores fueron realizados de la siguiente manera:
           - **-** Se implementaron dos funciones en el sprint 1 para la recopilación y el procesamiento de imágenes:

           - **--** La función "Imagenes" se encarga de leer la ruta de la imagen, el resize y la conversión a un arreglo de Numpy.

           ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/imge.PNG)


           - **--** La función "Data" se encarga de leer cada uno de los archivos xml que contienen los bounding boxes y clases de las imágenes etiquetadas. Asimismo, dentro de dicha función, se encuentra "Imagenes" para leerlo y realizar el procesamiento de las imágenes directamente.

         ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/data1.PNG)

         ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/data2.PNG)


          - **--** El preprocesamiento de las imágenes, como la normalización de las mismas (colocar cada píxel de la imagen en un rango de 0 a 1) se hace en la red neuronal. Es decir, la primera 'capa' de la red se encargará de realizar la normalización:

         ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/Rescaling.PNG)

    - Tarea 3: Implementar una red neuronal simple para la detección de objetos en un entorno local:
       - Creación de la arquitectura de la red neuronal


  - Sprint 2:
     - Tareas planificadas:
       - Tarea 1: Distribuir el procesamiento de imágenes utilizando técnicas de paralelismo:
          - Pool de procesos para la data de train y test
       - Tarea 2: Uso de GPU para mejora del tiempo en el entrenamiento de la red neuronal
       - Tarea 3: Cuantización post-entrenamiento de la red
