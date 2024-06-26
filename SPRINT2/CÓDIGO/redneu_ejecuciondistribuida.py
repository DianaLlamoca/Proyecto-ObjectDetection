# -*- coding: utf-8 -*-
"""RedNeu_EjecucionDistribuida.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vaXqk1Ijw8jxkkaqyfnkBNtEKDc2w9Pj
"""

!unzip /content/train.zip

!unzip /content/test.zip

# Importamos las librerías necesarias
import numpy as np
import xml.etree.ElementTree as ET
import os
from PIL import Image
import tensorflow
from keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, LeakyReLU, BatchNormalization
import cv2

# Se importan las librerías para implementar el paralelismo:
from concurrent import futures

# Cargamos las clases del dataset y le asignamos un número. Se guardán en forma de clave, valor en un diccionario.
clases = ["cat", "chicken", "cow", "dog", "fox", "goat", "horse", "person", "racoon", "skunk"]
etiquetas = {clase: ide for ide, clase in enumerate(clases)}


# Ahora, se crea una función para procesar las imágenes, ya que se hará un 'reshape' para que se tenga la misma forma en todas las img.
def Imagenes(path_img):
    # Se lee la imagen
    #Imagen=cv2.imread(path_img)

    #Se convierte el array de Numpy a una imagen de PIL
    #Imagen=Image.fromarray(Imagen)

    Imagen = Image.open(path_img).convert("RGB")  # Leemos las imágenes, pero en RGB
    #print("Imagen sin resize",Imagen)


    # Finalmente, se hace el resize para que cada imagen tenga la misma forma (se mantienen los 3 canales RGB)
    Imagen=Imagen.resize((224, 224))
    #Imagen = cv2.resize(Imagen,(224, 224))

    # Lo convertimos a un arreglo de numpy
    Imagen = np.array(Imagen)
    #print(Imagen.shape)
    #print("Imagen con resize",Imagen)

    return Imagen


# Debido a que las anotaciones del etiquetado están en un archivo XML, se procederá a extraer la información
# necesaria, como los bordes de las anotaciones y su clase correspondiente de la imagen. Para ello, se hará uso
# de la librería xml.etree.ElementTree
def Data(xml_ruta):
    # Creamos las listas donde se almacenará la imagen, los bordes de las anotaciones y clase
    targets=[]
    clase=[]
    imagen=[]

    # Ya que se tienen las rutas de los archivos xml, se procederá a obtener la información necesaria de cada uno de ellos
    # Sin embargo, antes de proceder con la lectura de los xml, debemos aprovechar que los nombres de las imgs son iguales al de los xlm,
    # así que también las leemos, ya que deben ser almacenadas para entrenar a la red neuronal
    img_ruta = xml_ruta.replace(".xml", ".jpg")  # cambiamos el .xml a .jpg para tener las rutas de cada imagen

    # Ya que se tiene la ruta de la imagen, la mandamos a procesar para realizar el resize mediante la función que creamos al inicio
    img = Imagenes(img_ruta)


     # Se lee el archivo xml
    arc_xml = ET.parse(xml_ruta)

    # Ahora, se obtiene el elemento "raíz" de ese archivo, para a partir de él iterar los demás elementos en el archivo xml
    elem_root = arc_xml.getroot()

    # Se procederá con la iteración,a partir del elemento raíz, en busca de la información que se quiere obtener
    # Se selecciona el elemento hijo "object" del elemento root, pues aquí se encuentra la información que buscamos
    for elem in elem_root.findall('object'):
        # Ya que nos situamos en "object", obtenemos la clase de la imagen, que está ubicada en "name" (en el archivo xml)
        etiq = elem.find('name').text

        # Sin embargo, lo que se quiere obtener es el valor numérico de dicha clase, entonces usamos el diccionario que creamos al inicio
        etiq_ide = etiquetas.get(etiq)

        # Obtenemos el ancho y alto de cada imagen
        width = int(elem_root.find('size').find('width').text)
        height = int(elem_root.find('size').find('height').text)

        # Obtenemos, ahora, las posiciones de los bordes donde se encuentran los objetos en las imágenes
        # Para ello, nos situamos dentro de "bndbox", que a su vez se encuentra dentro de "object"
        box = elem.find('bndbox')

        # Procedemos a obtener las posiciones correspondientes y se divide, pues se hizo un resize de la imagen
        xmin = int(int(box.find('xmin').text) / (width / 224))
        ymin = int(int(box.find('ymin').text) / (height / 224))
        xmax = int(int(box.find('xmax').text) / (width / 224))
        ymax = int(int(box.find('ymax').text) / (height / 224))

        # Ahora, guardamos cada uno de los datos en las listas "imagenes","targets", en donde mencionamos que serían almacenados
        targets.append([xmin, ymin, xmax, ymax])
        clase.append(etiq_ide)
        imagen.append(img)
    return targets, clase, imagen

if __name__=="__main__":
    # Para paralelizar el código, se necesitará una función que debe ser la "tarea" a asignar para cada proceso:
    train_path = "/content/train"
    test_path = "/content/test"

    # Se crean los arreglos donde se almacenarán las imágenes, targets (bounding boxes) y la clase
    imagenes_train = []
    targets_train = []
    clase_train = []

    imagenes_test = []
    targets_test = []
    clase_test = []

    # Obtenemos las rutas de solo los archivos xml para la lectura de los mismos
    xml_rutas_train = sorted(
        [os.path.join(train_path, direct) for direct in os.listdir(train_path) if direct.endswith(".xml")])
    xml_rutas_test = sorted(
        [os.path.join(test_path, direct) for direct in os.listdir(test_path) if direct.endswith(".xml")])

    #Distribuiyendo el procesamiento de imágenes utilizando técnicas de paralelismo: concurrent.futures para distribuir el procesamiento de imágenes en múltiples núcleos de CPU
    with futures.ProcessPoolExecutor() as executor:
        #A cada proceso se le asigna una ruta para que la lea y se haga el procesamiento
        for ruta in xml_rutas_train:
            l=executor.submit(Data,ruta)
            #Almacenamos el resultado de cada tarea hecha por cada proceso en las listas "targets" y "clase"
            targets_train.extend(l.result()[0]) #el índice 0 de la variable 'l' hace referencia al bounding box
            clase_train.extend(l.result()[1])   #el índice 1 de la variable 'l' hace referencia a la clase
            imagenes_train.extend(np.array(l.result()[2])) #el índice 2 de la variable 'l' hace referencia a la imagen (en array)


    #Se realiza lo mismo para la data de test
    with futures.ProcessPoolExecutor() as executor:
        for ruta in xml_rutas_test:
            l=executor.submit(Data,ruta)
            targets_test.extend(l.result()[0])
            clase_test.extend(l.result()[1])
            imagenes_test.extend(np.array(l.result()[2])) #En array

    #Finalmente, para ver si se guardó en las listas "targets" y "clase", se imprimirá su longitud, que debería ser mayor a 0
    print("Tamaño de targets_train:",len(targets_train))
    print("Tamaño de clase_train",len(clase_train))
    print("Tamaño de imagenes_train",len(imagenes_train))

    print("Tamaño de targets_test",len(targets_test))
    print("Tamaño de clase_test",len(clase_test))
    print("Tamaño de imagenes_test",len(imagenes_test))

##------------------##
    #Una vez que la data ya se tiene, se convertirán a arreglos de numpy
    targets_train=np.array(targets_train)
    clase_train=np.array(clase_train)
    imagenes_train=np.array(imagenes_train)

    targets_test=np.array(targets_test)
    clase_test=np.array(clase_test)
    imagenes_test=np.array(imagenes_test)


    #Guardamos la data en variables representativas
    x_train,y_train,ytrain_clase=imagenes_train,targets_train,clase_train
    x_test,y_test,ytest_clase=imagenes_test,targets_test,clase_test

# Ya que la data está preprocesada, se procederá a crear la arquitectura de la red, haciendo uso del entrenamiento distribuido
# en Keras.

#Para ello, primero se comprueba si hay gpu's disponibles
gpus = tensorflow.config.list_physical_devices('GPU')
if gpus:
    print("GPU está disponible")
else:
    print("GPU no está disponible")

#Debido a que la GPU sí está disponible, se procederá a ver cuántas GPU hay en el sistema, entonces
dispositivo = '/GPU:0' if tensorflow.config.list_physical_devices('GPU') else '/CPU:0'
num_gpus = len(tensorflow.config.list_physical_devices('GPU'))
print("Dispositivo:",dispositivo)
print("Número de GPU's:",num_gpus)

#Si bien solo hay una GPU disponible, igual se realizará la arquitectura de la red como si hubiesen múltiples GPU.
#De esta manera, si existieran más GPU disponibles, la red pueda ser entrenada en un entorno distribuido.

#Para ello, se creará un objeto "MirroredStrategy", el cual proporciona una abstracción para distribuir en varias unidades de procesamiento.
strategy = tensorflow.distribute.MirroredStrategy()
print("strategy objeto:",strategy)

#Para hacer más ordenado el código, se creará una función que se encargará de definir las funciones de pérdida para
#cada una de las "ramas de salida". Además, también se define el optimizador. En este caso, "Adam":
def FuncP_Opti():
    func_perd = {
        "cl_head": tensorflow.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        "bb_head": tensorflow.keras.losses.MeanSquaredError()
    }
    optimizador = Adam()
    return func_perd, optimizador

#Según la documentación de keras, se crea y compila el modelo en el contexto de strategy.scope
#Ahora, se define la red neuronal con dicha estrategia de distribución:
with strategy.scope():
  # Debido a que la detección de objetos necesita de clasificación y regresión para obtener los bounding boxes, se creará, primero,
  # la arquitectura compartida
  data_input = (224, 224, 3)  # Pues las imágenes son de esa dimensión
  input_layer = tensorflow.keras.layers.Input(data_input)  # Esta es la capa de entrada

  # Se crean, ahora, las capas bases
  # La primera capa se encargará de realizar la normalización y luego las capas para la extracción de características
  capas_base = layers.Rescaling(scale=1. / 255, name="capa_base1")(input_layer)
  capas_base = layers.Conv2D(32, 3, padding="same", activation="relu", name="capa_base2")(capas_base)
  capas_base = layers.MaxPooling2D(name="capa_base3")(capas_base)
  capas_base = layers.BatchNormalization()(capas_base)
  capas_base = layers.Conv2D(32, 3, padding="same", activation="relu", name="capa_base4")(capas_base)
  capas_base = layers.BatchNormalization()(capas_base)
  capas_base = layers.Conv2D(32, 3, padding="same", activation="relu")(capas_base)
  capas_base = layers.MaxPooling2D(name="capa_base5")(capas_base)
  capas_base = layers.BatchNormalization()(capas_base)
  capas_base = layers.Conv2D(32, 3, padding="same", activation="relu", name="capa_base6")(capas_base)
  capas_base = layers.MaxPooling2D(name="capa_base7")(capas_base)
  capas_base = layers.BatchNormalization()(capas_base)
  capas_base = layers.Conv2D(32, 3, padding="same", activation="relu", name="capa_base8")(capas_base)
  capas_base = layers.MaxPooling2D(name="capa_base9")(capas_base)
  capas_base = layers.Flatten(name="capa_base10")(
      capas_base)  # La capa de entrada a la red full connected (acá se obtienen vectores)

  # Ahora, a partir de la capa de Flatten, se crearán las capas para la clasificación
  clasificacion = layers.Dense(128, activation="relu", name="c_clas1")(capas_base)
  clasificacion = layers.Dense(10, name="cl_head")(clasificacion)  # 10 neuronas, pues son 10 clases

  # Ahora, se definen las capas para predecir los bounding boxes a partir de la capa de flatten (igual que el paso anterior)
  boundingb = layers.Dense(128, activation="relu", name="c_boundb1")(capas_base)
  boundingb = layers.Dense(64, activation="relu", name="c_boundb2")(boundingb)
  boundingb = layers.Dense(32, activation="relu", name="c_bound3")(boundingb)
  boundingb = layers.Dense(4, activation="linear", name="bb_head")(
      boundingb)  # 4 neuronas que representan a los bounding boxes

  # Finalmente, se define el modelo final con las 2 capas de salida (clasificación y bounding boxes)
  modelo = tensorflow.keras.Model(input_layer,
                                  outputs=[clasificacion, boundingb])

#Ya que la arquitectura ha sido definida, se mostrará el "summary" de la red neuronal:
modelo.summary()

#De la misma forma, usando dicha estrategia de distribución.
#Recordar que, según la documentación de keras, se crea y compila el modelo en el contexto de strategy.scope

#Para ello, primero debemos obtener las funciones de pérdida, para cada rama, que se ha definido previamente; así como el optimizador:
func_perd, opti = FuncP_Opti()

#Se compila el modelo usando la est. de dist.:
with strategy.scope():
    modelo.compile(loss=func_perd, optimizer=opti,
                   metrics={"cl_head": "accuracy",
                            "bb_head": tensorflow.keras.metrics.MeanSquaredError()})

#Ahora, lo que se va a realizar, es definir cuáles son los targets para cada rama de salida de la red neuronal:
# la rama dedicada a predecir los bounding boxes, así como la rama dedicada a predecir la clase
train_targets = {
    "cl_head": ytrain_clase,
    "bb_head": y_train
}
test_targets = {
    "cl_head": ytest_clase,
    "bb_head": y_test
}

#Ya que se tiene definido lo anterior, se procederá con el entrenamiento del modelo de la manera habitual, llamando a Model.fit en el
#modelo y pasando el conjunto de datos, pues este paso es el mismo ya sea que esté distribuyendo o no.

#El número de épocas será 150 (aunque se pueden colocar más épocas). El tamaño del batch será 4
modelo.fit(x_train, train_targets,
             validation_data=(x_test, test_targets),
             batch_size=4,
             epochs=150,
             shuffle=True,
             verbose=1)