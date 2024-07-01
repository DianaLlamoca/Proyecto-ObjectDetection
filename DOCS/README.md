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
- **Informe detallado del proceso de desarrollo**:
  a) **OBTENCIÓN DE LOS DATOS: RECOPILACIÓN DE IMÁGENES**

El conjunto de imágenes fue dividido en datos de *training* y *testing*:

* Datos de *training*:
  Consta de 1400 archivos. Cada imagen tiene su archivo 'xml' correspondiente, los cuales contienen la clase del objeto que está en la imagen, así como el 
  *bounding box*. Es decir, el archivo 'xml' es el archivo que contiene toda la información de la imagen ya etiquetada.
  La data de training consta de 700 imágenes.
  
* Datos de *testing*:
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


**--** El preprocesamiento de las imágenes, como la normalización de las mismas (colocar cada píxel de la imagen en un rango de 0 a 1) se hace en la red neuronal. Es decir, la primera 'capa' de la red se encargará de realizar la normalización:

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
