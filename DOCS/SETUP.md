# INSTRUCCIONES PARA CONFIGURAR EL ENTORNO

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
