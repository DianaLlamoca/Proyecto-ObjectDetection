# Introducción: Comienza con una introducción que resuma el proyecto, sus objetivos y su relevancia
## Resumen del proyecto:
El proyecto consiste en desarrollar un sistema distribuido de visión computacional para detectar objetos en imágenes. EL modelo de red neuronal debe realizar el problema de clasificación para detectar las clases en la imagen dada; asimismo, calculará las coordenadas de los bounding boxes que indican en dónde se encuentra el objeto. Además, para optimizar la escalabilidad y mejorar la eficiencia del entrenamiento de la red neuronal, se hará uso de la computación paralela y distribuida. De esta forma, cada 'nodo' se encargará de realizar un determinado trabajo, en paralelo con el resto, para optimizar el funcionamiento general del sistema.

## Objetivos:
### Sprint 1:
• Configurar el entorno de desarrollo con las bibliotecas necesarias.

• Recopilar y preprocesar un conjunto de datos de imágenes.

• Implementar una red neuronal simple para la detección de objetos en un entorno local.

### Sprint 2:
• Distribuir el procesamiento de imágenes utilizando técnicas de paralelismo.

• Implementar una cola de tareas para gestionar el procesamiento de imágenes.

• Optimizar la red neuronal para ejecución distribuida
