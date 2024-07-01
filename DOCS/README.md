# PROYECTO:  SISTEMA DE VISIÓN COMPUTACIONAL DISTRIBUIDO PARA DETECCIÓN DE OBJETOS
# OBJETIVO DEL PROYECTO
Desarrollar un sistema distribuido de visión computacional para la detección de objetos en imágenes, optimizando la escalabilidad y la eficiencia del procesamiento.

# DESCRIPCIÓN GENERAL
El proyecto consiste en desarrollar un sistema distribuido de visión computacional para detectar objetos en imágenes. EL modelo de red neuronal debe realizar el problema de clasificación para detectar las clases en la imagen dada; asimismo, calculará las coordenadas de los *bounding boxes* que indican en dónde se encuentra el objeto.
Además, para optimizar la escalabilidad y mejorar la eficiencia del entrenamiento de la red neuronal, se hará uso de la computación paralela y distribuida. De esta forma, cada 'nodo' se encargará de realizar un determinado trabajo, en paralelo con el resto, para optimizar el funcionamiento general del sistema.


# INSTRUCCIONES PARA CONFIGURAR EL ENTORNO Y EJECUCIÓN DEL PROYECTO

## LIBRERÍAS UTILIZADAS:
Las librerías que se usaron fueron las siguientes:
- **Numpy**: Se usó 'numpy' para tratar la data como arreglos/matrices de numpy y así mejorar la eficiencia en las operaciones.
- **xml**: Se usó 'xml' para la lectura de los archivos xml, pues estos contienen los *labels*, donde se encuentra la información de las coordenadas de los *bounding boxes* de los objetos en las imágenes.
- **os**: Se usó 'os' para realizar las operaciones relacionadas a la gestión/manejo de archivos, como directorios, ya que estos últimos son los que contienen las imágenes.
- **PIL**: Se usó 'PIL' para algunas operaciones sobre las imágenes.
- **opencv**: Se usó "opencv" para realizar 'operaciones' sobre las imágenes, como dibujar el bounding box de las coordenadas predichas por el modelo para el objeto en las imágenes de test.
- **tensorflow**: Se usó 'tensorflow' para la creación de la arquitectura de la red neuronal convolucional.
- **concurrent.futures**: Se usó "concurrent.futures" para crear un Pool de procesos, de tal forma que a cada uno se le asigne una tarea y estas sean ejecutadas en paralelo.

## Para configurar el entorno, se deben seguir los siguientes pasos:
- 1) Crear el entorno virtual para instalar las librerías necesarias: 'python3 -m venv nombre_del_directorio_del_entorno'
-  2) Activar el entorno: 'source bin/activate'
- 3) Dentro del entorno, instalar cada una de las bibliotecas  que requieran de instalación, puesto que algunas ya están implementadas por defecto en Python:
     * pip install numpy
     * pip install tensorflow
     * pip install futures
- 4) Luego, crear un archivo de extensión '.py' en donde se colocará el código.
- 5) Ejecutar el código haciendo uso de 'python3 *nombre_del_archivo.py*'
 
# INFORME
## **Informe detallado del proceso de desarrollo**:
  
  a) **OBTENCIÓN DE LOS DATOS: RECOPILACIÓN DE IMÁGENES**

  El conjunto de imágenes fue dividido en datos de *training* y *testing*:

  - Datos de *training*:
  Consta de 1400 archivos. Cada imagen tiene su archivo 'xml' correspondiente, los cuales contienen la clase del objeto que está en la imagen, así como el 
  *bounding box*. Es decir, el archivo 'xml' es el archivo que contiene toda la información de la imagen ya etiquetada.
  La data de training consta de 700 imágenes.
  
  - Datos de *testing*:
  Consta de 194 archivos (imágenes + xml) para evaluar el *performance* de la red neuronal luego de su entrenamiento. 

  b) **PREPROCESAMIENTO DEL CONJUNTO DE IMÁGENES**

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


  **--** El preprocesamiento de las imágenes, como la normalización de las mismas (colocar cada píxel de la imagen en un rango de 0 a 1) se hace en la red 
  neuronal. Es decir, la primera 'capa' de la red se encargará de realizar la normalización:

  ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/Rescaling.PNG)

  c) **IMPLEMENTACIÓN DE LA RED NEURONAL**

  ### **ARQUITECTURA DE LA RED NEURONAL:**
  **-Capas de convolución:** 5 capas de convolución con un kernel de 3. A cada capa se le aplica el padding, de tal forma que cuando se apliquen cada uno de los filtros a las imágenes, la matriz resultante no se reduzca en forma, es decir, tenga el mismo shape que la matriz de entrada

  **- Capas de MaxPooling:** Luego de cada capa de convolución, se le aplica la capa de MaxPooling --> 5 capas de MaxPooling. Las capas de MaxPooling se encargarán de extraer los píxeles con 'mayor relevancia' (píxeles de mayor valor en la matriz de salida) luego de haber aplicado los filtros a cada una de las imágenes en las capas de convolución; de esta forma, la matriz se hace más pequeña y, por lo tanto, más eficiente serán las operaciones para las próximas capas, puesto que el shape de la matriz de entrada se va reduciendo.

  **- Capas de BatchNormalization:** 4 capas de BatchNormalization. Las capas de 'normalización' (batch normalization) se encargarán de 'centrar' y 'normalizar' cada mini-batch que llega a la red, añadiendo el hecho de que también introduce cierto ruido que actúa como regularización y así prevenir el overfitting.

  **- Capas lineales:**

  **-** 2 capas densas (lineales) para la clasificación.

  **-** 4 capas densas (lineales) para la regresión.

**Red neuronal**:
![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/rn.PNG)


## LAS DECISIONES TOMADAS
Las decisiones, para implementar algunas técnicas de paralelismo y hacer más eficiente el entrenamiento de la red neuronal, fueron las siguientes:
## * Decisión 1: Distribuir el procesamiento de imágenes utilizando técnicas de paralelismo
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
    
  
  
## * Decisión 2: Uso de GPU para mejora del tiempo en el entrenamiento de la red neuronal:
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


## * Decisión 3: Cuantización post-entrenamiento de la red:
• Debido a que el modelo ha sido entrenado, se aplicarán técnicas de cuantización, pero posterior al entrenamiento.
  La cuantización, lo que va a hacer, es que el modelo va a ser reducido en tamaño, y así más apto para dispositivos que tienen menos memoria.
  De esta forma, la velocidad de "inferencia" en la red neuronal puede también mejorar, pues dicha operación es costosa computacionalmente
  ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/cuantizado_mod.PNG)
 
  El tamaño del modelo cuantizado se redujo significativamente. El cuantizado que se usó, lo que hará es transformar todos los pesos de la red en números enteros. 
  De esta manera, se usará menos espacio en memoria, lo cual puede impactar en el tiempo de procesamiento, y así hacerlo más eficiente. Sin embargo, puede afectar 
  la precisión del modelo, al haber una variación en los pesos. 


## LOS PROBLEMAS ENCONTRADOS
• **Desafíos encontrados:**
 - Al querer implementar la **cuantización de modelos** como técnica de optimización y luego evaluar el impacto de las optimizaciones en la precisión y el tiempo 
   de procesamiento tuve dificultades en la "cuantización aware-training".
   - **Cuantización aware-training**: Esta forma de cuantización, según la documentación de TensorFlow, suele ser mejor para la precisión del modelo. Por ello, 
     intenté aplicar esta forma de cuantización para posteriormente calcular el performance:
     
     •![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/a_t1.PNG)
     •![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/a_t2.PNG)
     •![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/a_t3.PNG)
     •![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/a_t4.PNG)
     Debido a este error, intenté colocar dicha capa que generaba el error dentro de "quantize_scope"
     •![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT2/IM%C3%81GENES/a_t5.png)
   Traté de solucionarlo, pero no pude encontrar la solución. Por ese motivo, no pude lograr comparar el performance del modelo al aplicarle la cuantización.


## ANÁLISIS DE RESULTADOS Y MÉTRICAS:
- **Prueba: Se entrenó al modelo con 10 épocas sin considerar GPU.**
      *  Se utilizaron 4 imágenes de prueba para evaluar los valores predichos por el modelo.
  
      * **Accuracy para el problema de clasificación**: 13.19444477558136 %
  
      * **MSE para el problema de bounding boxes**: 1816.4044189453125
  
      * Resultados:
      * Imagen de prueba 1 con resultados:
          ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_1.PNG)

    * Imagen de prueba 2 con resultados:
  
      *   ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_2.PNG)
      
    * Imagen de prueba 3 con resultados:
      
      *   ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_3.PNG)
      
    * Imagen de prueba 4 con resultados:
      *   ![](https://github.com/DianaLlamoca/Proyecto-ObjectDetection/blob/main/SPRINT1/IM%C3%81GENES/ev_4.PNG)
