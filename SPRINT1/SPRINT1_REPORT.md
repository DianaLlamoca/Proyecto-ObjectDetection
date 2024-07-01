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


**--** El preprocesamiento de las imágenes, como la normalización de las mismas (colocar cada píxel de la imagen en un rango de 0 a 1) se hace en la red neuronal. Es decir, la primera 'capa' de la red se encargará de realizar la normalización:

![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/Rescaling.PNG)

## • **Tarea 3: Implementar una red neuronal simple para la detección de objetos en un entorno local**

### **ARQUITECTURA DE LA RED NEURONAL:**
**-Capas de convolución:** 5 capas de convolución con un kernel de 3. A cada capa se le aplica el padding, de tal forma que cuando se apliquen cada uno de los filtros a las imágenes, la matriz resultante no se reduzca en forma, es decir, tenga el mismo shape que la matriz de entrada

**- Capas de MaxPooling:** Luego de cada capa de convolución, se le aplica la capa de MaxPooling --> 5 capas de MaxPooling. Las capas de MaxPooling se encargarán de extraer los píxeles con 'mayor relevancia' (píxeles de mayor valor en la matriz de salida) luego de haber aplicado los filtros a cada una de las imágenes en las capas de convolución; de esta forma, la matriz se hace más pequeña y, por lo tanto, más eficiente serán las operaciones para las próximas capas, puesto que el shape de la matriz de entrada se va reduciendo.

**- Capas de BatchNormalization:** 4 capas de BatchNormalization. Las capas de 'normalización' (batch normalization) se encargarán de 'centrar' y 'normalizar' cada mini-batch que llega a la red, añadiendo el hecho de que también introduce cierto ruido que actúa como regularización y así prevenir el overfitting.

**- Capas lineales:**

**-** 2 capas densas (lineales) para la clasificación.

**-** 4 capas densas (lineales) para la regresión.

**Red neuronal**:
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/rn.PNG)

==========
# 3) IMPLEMENTACIÓN:
* **Descripción del trabajo realizado:**
  Hasta el momento, en el sprint 1 se recopiló el conjunto de datos de imágenes. Luego, se configuró las librerías necesarias, tanto para la lectura de las 
  imágenes, así como para obtener los datos relevantes de cada archivo xml (los bounding boxes de las imágenes y su clase correspondiente).
  Posteriormente, se creó la arquitectura de la red neuronal. Para crearla, fue necesario no usar la clase "Sequential" de Keras, ya que esto implicaría crear una 
  arquitectura de red lineal, y el objetivo es crear una red que tenga dos outputs (o ramas de salida), una para clasificación y la otra para 
  regresión, y así entrenar a la red para que realice cada una de esas tareas.
  
* **Algoritmos y métodos: Descripción de los algoritmos y métodos implementados.**
  
  *Funciones de pérdida*:
  - *SparseCategoricalCrossEntropy* para la rama que se encargará de la clasificación.
  - *MeanSquaredError* para la rama que se encargará del problema de regresión, para la predicción de los *bounding boxes*
  
  *Optimizador*:
  - El optimizador que se usó fue Adam para el entrenamiento de la red neuronal.
 
  *Métricas*:
  - *Accuracy* para la rama del problema de clasificación.
  - *MeanSquaredError* para la rama del problema de regresión.

# 4) RESULTADOS:
* **Funcionalidades desarrolladas: Lista de las funcionalidades que se desarrollaron durante el sprint**
  - Funciones que se encargan de la lectura y procesamiento de las imágenes para el entrenamiento de la red.
  - La arquitectura de la red neuronal.

* **Pruebas realizadas**
  Las GPU están diseñadas con una gran cantidad de núcleos que pueden realizar múltiples operaciones simultáneamente.
  Las GPU tienen miles de núcleos más pequeños y eficientes diseñados para tareas paralelas. Esta arquitectura permite a las GPU manejar las operaciones 
  matriciales y vectoriales que son fundamentales para el entrenamiento de redes neuronales de manera mucho más eficiente.
  Sin embargo, **en el primer sprint no se usó GPU**, puesto que ello se realizará en el siguiente sprint, donde se indica el "uso eficiente de GPU".
  
  - **1)** Entrenamiento de la red sin GPU y con 10 épocas:
    - **Prueba 1: 10 épocas sin GPU**:
      - Tiempo de entrenamiento: 12 minutos para 10 épocas
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/time.PNG)
      - Resultados al evaluar el modelo en la data de test con 10 épocas sin GPU:
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/10epctest.PNG)
      
  - **2)** Entrenamiento de la red sin GPU y con 20 épocas:
    - **Prueba 2: 20 épocas sin GPU**:
      - Tiempo de entrenamiento: 24 minutos para 20 épocas
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/20epc.PNG)
    - Resultados de evaluar el modelo en la data de train con 20 épocas sin GPU ():
      ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/20epceval.PNG)

  • **Demostración de funcionalidades**

    Para evaluar los datos predichos por el modelo, creé el código para generar las imágenes, con sus bounding boxes y clase predichos:
    ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/cod_ev.PNG)

   
    - **Prueba: Se entrenó al modelo con 10 épocas sin considerar GPU.**
      *  Se utilizaron 4 imágenes de prueba para evaluar los valores predichos por el modelo.
      * **Accuracy para el problema de clasificación**: 13.19444477558136 %
      * **MSE para el problema de bounding boxes**: 1816.4044189453125
      * **Resultados**
        - Imagen de prueba 1 con resultados:
          
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_1.PNG)
          
        - Imagen de prueba 2 con resultados:
          
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_2.PNG)
          
        - Imagen de prueba 3 con resultados:
          
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_3.PNG)
          
        - Imagen de prueba 4 con resultados:
          
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_4.PNG)

# 5) ANÁLISIS Y EVALUACIÓN:
# *Comparación con los objetivos del Sprint: Evaluación de cómo el trabajo realizado se compara con los objetivos iniciales del sprint*
- Tareas implementadas:
  - Configuración del entorno
  - Preprocesamiento de imágenes
  - Creación de la arquitectura de la red neuronal

# *Lecciones aprendidas: Reflexión sobre las lecciones aprendidas durante el sprint, incluyendo qué funcionó bien y qué se podría mejorar*
**Lecciones aprendidas**:
- El procesamiento de las imágenes juega un papel crucial para el entrenamiento de la red neuronal. Por lo que una mayor variedad de las mismas son fundamentales para que la red se entrene de mejor manera y generalice bien.
- La arquitectura de la red neuronal, que incluye las capas de convolución y MaxPooling, pueden determinar qué tan bien la red puede captar características (extracción de características) relevantes después de cada filtro o convolución aplicado.
- El uso de GPU es crucial para el entrenamiento de la red. Esta genera mayor rapidez durante el entrenamiento de la red neuronal; sin embargo, si solo se usa CPU, el proceso de entrenamiento tardará más, como fue el caso en este sprint 1.
  
**Lo que funcionó bien**:
- Las funciones para el preprocesamiento de los datos cumplían el rol que se quizo lograr en un principio.
- Si bien la red no tuvo una buena precisión, se logró crear una arquitectura de red neuronal para los dos problemas en la detección de objetos: clasificación 
  para identificar el objeto que se encuentra en la imagen, así como el problema de regresión para que la red pueda predecir los valores de los *bounding boxes* 
  para el objeto presente en la imagen.

**Lo que se podría mejorar**:
- Lo que se podría mejorar es el tiempo de entrenamiento que la red se demoró para el entrenamiento con solo 10 épocas. Lo anteriormente mencionado se puede 
  mejorar haciendo uso de la GPU, la unidad de procesamiento ideal para manejar las operaciones matriciales y vectoriales, fundamentales en la etapa de *training* 
  para ajustar los pesos de la red neuronal. *En el siguiente sprint se hará uso del GPU y se comparará el tiempo tomado*

  
