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
• Acá se ajustó la arquitectura de la red neuronal para mejorar el rendimiento en un entorno distribuido, teniendo en cuenta el número de GPU's disponibles.

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU1.PNG)

• Se usó "*tensorflow.distribute.MirroredStrategy()*", el cual proporciona una abstracción para realizar la ejecución distribuida en varias unidades de procesamiento.
Esta estrategia se utiliza normalmente para entrenar en una máquina con varias GPU.

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU2.PNG)

• Una vez que ya fue creado dicho objeto que representa a la estrategia usada, es importante mencionar que al utilizar estrategias de distribución, toda la creación de variables debe realizarse dentro del alcance de la estrategia. Esto replicará las variables en todas las réplicas y las mantendrá sincronizadas mediante un algoritmo de reducción total.

Por ese motivo, se define la arquitectura de la red neuronal dentro de la declaración *with* para asegurar lo anterior:
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU3.PNG)

• De la misma forma, la etapa de compilación, donde se especifican las funciones de pérdidas a usar, así como las métricas para evaluar la precisión del modelo, también debe de estar dentro del alcance de la estrategia. Se logra lo anterior, mediante la sentencia *with* en Python:
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU4.PNG)


Esta estrategia funciona de la siguiente manera: Esencialmente, se copia todas las variables del modelo a cada GPU. Luego, se usa "all-reduce" para combinar los gradientes de todos los GPU y aplica el valor combinado a todas las copias del modelo.
