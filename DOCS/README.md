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
