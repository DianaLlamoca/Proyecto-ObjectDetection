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

# METODOLOGÍA: Explica brevemente la metodología utilizada, incluyendo el enfoque ágil y la estructura de los sprints.
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

# DESARROLLO DEL PROYECTO: Desglosa el desarrollo del proyecto por sprints, destacando los objetivos y logros de cada sprint.
- **SPRINT 1:**
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
           -  Se implementaron **dos funciones** en el sprint 1 para la recopilación y el procesamiento de imágenes:

             -  La **función "Imagenes"** se encarga de leer la ruta de la imagen, el resize y la conversión a un arreglo de Numpy.

             ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/imge.PNG)


             - **--** La **función "Data"** se encarga de leer cada uno de los archivos xml que contienen los bounding boxes y clases de las imágenes etiquetadas. Asimismo, dentro de dicha función, se encuentra "Imagenes" para leerlo y realizar el procesamiento de las imágenes directamente.

           ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/data1.PNG)

           ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/data2.PNG)


            -  El preprocesamiento de las imágenes, como la normalización de las mismas (colocar cada píxel de la imagen en un rango de 0 a 1) se hace en la 
  red neuronal. Es decir, la primera 'capa' de la red se encargará de realizar la normalización:

           ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/Rescaling.PNG)

    - Tarea 3: Implementar una red neuronal simple para la detección de objetos en un entorno local:
       - Creación de la arquitectura de la red neuronal:
         
         - **Arquitectura de la red neuronal:**
           
            **-Capas de convolución:** 5 capas de convolución con un kernel de 3. A cada capa se le aplica el padding, de tal forma que cuando se apliquen cada uno de los filtros a las imágenes, la matriz resultante no se reduzca en forma, es decir, tenga el mismo shape que la matriz de entrada

             **- Capas de MaxPooling:** Luego de cada capa de convolución, se le aplica la capa de MaxPooling --> 5 capas de MaxPooling. Las capas de MaxPooling se encargarán de extraer los píxeles con 'mayor relevancia' (píxeles de mayor valor en la matriz de salida) luego de haber aplicado los filtros a cada una de las imágenes en las capas de convolución; de esta forma, la matriz se hace más pequeña y, por lo tanto, más eficiente serán las operaciones para las próximas capas, puesto que el shape de la matriz de entrada se va reduciendo.

             **- Capas de BatchNormalization:** 4 capas de BatchNormalization. Las capas de 'normalización' (batch normalization) se encargarán de 'centrar' y 'normalizar' cada mini-batch que llega a la red, añadiendo el hecho de que también introduce cierto ruido que actúa como regularización y así prevenir el overfitting.

            **- Capas lineales:**

             **-** 2 capas densas (lineales) para la clasificación.

             **-** 4 capas densas (lineales) para la regresión.

           **Red neuronal**:
           ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/rn.PNG)


  - **SPRINT 2**:
     - Tareas planificadas:
       - **Tarea 1: Distribuir el procesamiento de imágenes utilizando técnicas de paralelismo:**
          - Pool de procesos para la data de train y test:
            
            En las funciones encargadas a realizar el procesamiento de las imágenes (funciones "Imagenes" y "Data" del primer sprint") se aplicó el paralelismo para distribuir el procesamiento de imágenes a cada proceso:
         

              - **Pool de procesos para la data de *train***: Se creó un Pool de procesos usando la librería "concurrent.futures", de tal forma que a cada proceso se le asigna una ruta para que la lea y se haga el procesamiento:
    ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/p1.PNG)


              - **Pool de procesos para la data de *test***: Se creó un Pool de procesos usando la librería "concurrent.futures", de tal forma que a cada proceso se le asigna una ruta para que la lea y se haga el procesamiento:
    ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/p_.PNG)
 
    
       - **Tarea 2: Uso de GPU para mejora del tiempo en el entrenamiento de la red neuronal**
         - Acá se ajustó la arquitectura de la red neuronal para mejorar el rendimiento en un entorno distribuido, teniendo en cuenta el número de GPU's disponibles.
         ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU1.PNG)

         - Se usó "*tensorflow.distribute.MirroredStrategy()*", el cual proporciona una abstracción para realizar la ejecución distribuida en varias unidades de procesamiento. Esta estrategia se utiliza normalmente para entrenar en una máquina con varias GPU.
         ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU2.PNG)

         - Una vez que fue creado dicho objeto que representa a la estrategia usada, es importante mencionar que al utilizar estrategias de distribución, toda la creación de variables debe realizarse dentro del alcance de la estrategia. Esto replicará las variables en todas las réplicas y las mantendrá sincronizadas mediante un algoritmo de reducción total. Por ese motivo, se define la arquitectura de la red neuronal dentro de la declaración *with* para asegurar lo anterior:
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU3.PNG)

         - De la misma forma, la etapa de compilación, donde se especifican las funciones de pérdidas a usar, así como las métricas para evaluar la precisión del modelo, también debe de estar dentro del alcance de la estrategia. Se logra lo anterior, mediante la sentencia *with* en Python:
         
         ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/GPU4.PNG)
       
      
       - **Tarea 3: Cuantización post-entrenamiento de la red**

         Debido a que el modelo ha sido entrenado, se aplicarán técnicas de cuantización, pero posterior al entrenamiento.
         
         La cuantización, lo que va a hacer, es que el modelo va a ser reducido en tamaño, y así más apto para dispositivos que tienen menos memoria.
         De esta forma, la velocidad de "inferencia" en la red neuronal puede también mejorar, pues dicha operación es costosa computacionalmente:
         
         ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/cuantizado_mod.PNG)
         
         El tamaño del modelo cuantizado se redujo significativamente. El cuantizado que se usó, lo que hará es transformar todos los pesos de la red en números enteros. 
         De esta manera, se usará menos espacio en memoria, lo cual puede impactar en el tiempo de procesamiento, y así hacerlo más eficiente. Sin embargo, puede afectar la precisión del modelo, al haber una variación en los pesos. 

=======

# RESULTADOS Y DEMOSTRACIÓN: Presenta los resultados más importantes y realiza una demostración en vivo de las funcionalidades clave del proyecto
**PRUEBAS:**

- **Prueba 1: Se entrenó al modelo con 10 épocas sin considerar GPU.**
 - Se utilizaron 4 imágenes de prueba para evaluar los valores predichos por el modelo.
 - **Accuracy para el problema de clasificación**: 13.19444477558136 %
 - **MSE para el problema de bounding boxes**: 1816.4044189453125
 - **Resultados**
   - Imagen de prueba 1 con resultados: 

     ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_1.PNG)
          
   - Imagen de prueba 2 con resultados:
          
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_2.PNG)
          
   - Imagen de prueba 3 con resultados:
          
       ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_3.PNG)
          
    - Imagen de prueba 4 con resultados:
          
       ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_4.PNG)

- **Prueba 2: Se entrenó al modelo con 20 épocas sin considerar GPU.**
  - Se utilizaron 4 imágenes de prueba para evaluar los valores predichos por el modelo.
  - **Accuracy para el problema de clasificación**: 16.66666716337204 %
  - **MSE para el problema de bounding boxes**: 1560.8096923828125
  - **Resultados**
     - Imagen de prueba 1 con resultados:
          
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev2_1.PNG)
          
        - Imagen de prueba 2 con resultados:
          
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev2_2.PNG)
          
        - Imagen de prueba 3 con resultados:
          
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev2_3.PNG)
          
        - Imagen de prueba 4 con resultados:
          
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev2_4.PNG)

- **Prueba 3: Se entrenó al modelo con 10 épocas considerando GPU.**
  *  Se utilizaron 4 imágenes de prueba para evaluar los valores predichos por el modelo.
  * **Accuracy para el problema de clasificación**: 16.6 %
  * **MSE para el problema de bounding boxes**: 1753.95
  * **Resultados**
    - Imagen de prueba 1 con resultados:
  
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/res2_1.PNG)
          
    - Imagen de prueba 2 con resultados:
          
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/res2_2.PNG)
          
    - Imagen de prueba 3 con resultados:
          
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/res2_3.PNG)
          
    - Imagen de prueba 4 con resultados:
          
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/res2_4.PNG)

  - **Prueba 4: Se entrenó al modelo con 20 épocas considerando GPU.**
  *  Se utilizaron 4 imágenes de prueba para evaluar los valores predichos por el modelo.
  * **Accuracy para el problema de clasificación**: 16.6 %
  * **MSE para el problema de bounding boxes**: 1588.02
  * **Resultados**
    - Imagen de prueba 1 con resultados:
  
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/spr2_im1.PNG)
          
    - Imagen de prueba 2 con resultados:
          
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/spr2_im2.PNG)
          
    - Imagen de prueba 3 con resultados:
          
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/spr2_im3.PNG)
          
    - Imagen de prueba 4 con resultados:
          
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/spr2_im4.PNG)
      
=======

# ANÁLISIS Y EVALUACIÓN: Discute las lecciones aprendidas, los desafíos enfrentados y cómo se superaron.
  - **Lecciones aprendidas**:
    - El procesamiento de las imágenes juega un papel crucial para el entrenamiento de la red neuronal. Por lo que una mayor variedad de las mismas son fundamentales para que la red se entrene de mejor manera y generalice bien.
    - La arquitectura de la red neuronal, que incluye las capas de convolución y MaxPooling, pueden determinar qué tan bien la red puede captar características (extracción de características) relevantes después de cada filtro o convolución aplicado.
    - El uso de GPU es crucial para el entrenamiento de la red. Esta genera mayor rapidez durante el entrenamiento de la red neuronal; sin embargo, si solo se usa CPU, el proceso de entrenamiento tardará más, como fue el caso en este sprint 1.
    - Se pudo usar el paralelismo a nivel de datos, aplicando la misma instrucción (los pasos para el procesamiento de las imágenes) a un conjunto de datos, 
   repartiéndolo a cada proceso.
    - El uso de GPU puede acelerar exponencialmente si se compara a entrenar la red con una CPU.
    -La cuantización de modelos; en este caso, cuantización post-training, puede optimizar el uso de la memoria.

  - **Los desafíos enfrentados**:
    - La red no tuvo una buena precisión para la tarea de clasificación. En lo que respecta al tiempo de entrenamiento que la red se demoró, se pudo 
  mejorar haciendo uso de la GPU, la unidad de procesamiento ideal para manejar las operaciones matriciales y vectoriales, fundamentales en la etapa de *training* 
  para ajustar los pesos de la red neuronal. *En el siguiente sprint se hará uso del GPU y se comparará el tiempo tomado*.
    - Respecto a la cola de tareas, tuve dificultades para implementarla, pero considero que al implementar la cola de tareas y 
  configurarla para distribuir las cargas de trabajo entre múltiples trabajadores, haría mucho más eficiente el proceso.
  
    - En la cuantización aware-training también pudo haber impactado en las optimizaciones de la precisión y el tiempo de procesamiento. Sin embargo, tuve algunos 
   errores que no me permitieron aplicar dicha cuantización.

=======

# CONCLUSIÓN Y FUTURO TRABAJO: Concluye con un resumen de los logros y posibles mejoras o expansiones futuras del proyecto
- **Logros**:
  - Las funciones para el preprocesamiento de los datos cumplían el rol que se quizo lograr en un principio.
  - Si bien la red no tuvo una buena precisión, se logró crear una arquitectura de red neuronal para los dos problemas en la detección de objetos: clasificación 
  para identificar el objeto que se encuentra en la imagen, así como el problema de regresión para que la red pueda predecir los valores de los *bounding boxes* 
  para el objeto presente en la imagen.
  - Se pudo asignar una tarea a cada proceso, funcionando así el paralelismo a nivel de datos.
  - El tiempo de entrenamiento usando GPU fue mejorado.
  - El espacio que ocupa en memoria el modelo se logró, al aplicar la cuantización post-training al modelo.

- **Mejoras**:
  - Lo que podría mejorar es implementar la cola de tareas. Tuve dificultades para implementarlo, pero considero que al implementar la cola de tareas y 
  configurarla para distribuir las cargas de trabajo entre múltiples trabajadores, haría mucho más eficiente el proceso
 
  - La cuantización aware-training también pudo haber impactado en las optimizaciones de la precisión y el tiempo de procesamiento. Sin embargo, tuve algunos 
   errores que no me permitieron aplicar dicha cuantización.
