#Importamos las librerías necesarias
import numpy as np
import xml.etree.ElementTree as ET
import os
from PIL import Image
import tensorflow
from keras import layers
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout,LeakyReLU, BatchNormalization


#Cargamos las clases del dataset y le asignamos un número. Se guardán en forma de clave, valor en un diccionario.
clases=["cat","chicken","cow","dog","fox","goat","horse","person","racoon","skunk"]
etiquetas={clase:ide for ide,clase in enumerate(clases)}

#Ahora, se crea una función para procesar las imágenes, ya que se hará un 'reshape' para que se tenga la misma forma en todas las img.
def Imagenes(path_img):
    #Se lee la imagen
    #Imagen=cv2.imread(path_img)
    Imagen=Image.open(path_img).convert("RGB") #Leemos las imágenes, pero en RGB

    #Finalmente, se hace el resize para que cada imagen tenga la misma forma (se mantienen los 3 canales RGB)
    Imagen=Imagen.resize((224,224))

    #Lo convertimos a un arreglo de numpy
    Imagen=np.array(Imagen)

    return Imagen

#Debido a que las anotaciones del etiquetado están en un archivo XML, se procederá a extraer la información
#necesaria, como los bordes de las anotaciones y su clase correspondiente de la imagen. Para ello, se hará uso
#de la librería xml.etree.ElementTree
def Data(root_path):
    #Creamos dos listas, una donde se almacenará la imagen y la otra contendrán las variables objetivos (bordes de las anotaciones, clase)
    imagenes=[]
    targets=[]

    clase=[]

    #Obtenemos las rutas de solo los archivos xml para la lectura de los mismos
    xml_rutas=sorted([os.path.join(root_path,direct) for direct in os.listdir(root_path) if direct.endswith(".xml")])


    #Ya que se tienen las rutas de los archivos xml, se procederá a obtener la información necesaria de cada uno de ellos
    #Se recorre cada uno de los archivos xml
    for xml in xml_rutas:
        #Sin embargo, antes de proceder con la lectura de los xml, debemos aprovechar que los nombres de las imgs son iguales al de los xlm,
        #así que también las leemos, ya que deben ser almacenadas para entrenar a la red neuronal
        img_ruta=xml.replace(".xml",".jpg") #cambiamos el .xml a .jpg para tener las rutas de cada imagen
        
        #Ya que se tiene la ruta de la imagen, la mandamos a procesar para realizar el resize mediante la función que creamos al inicio
        img=Imagenes(img_ruta)

        #Se lee el archivo xml
        arc_xml=ET.parse(xml)

        #Ahora, se obtiene el elemento "raíz" de ese archivo, para a partir de él iterar los demás elementos en el archivo xml
        elem_root=arc_xml.getroot()

        #Se procederá con la iteración,a partir del elemento raíz, en busca de la información que se quiere obtener
        #Se selecciona el elemento hijo "object" del elemento root, pues aquí se encuentra la información que buscamos
        for elem in elem_root.findall('object'):

            #Ya que nos situamos en "object", obtenemos la clase de la imagen, que está ubicada en "name" (en el archivo xml)
            etiq=elem.find('name').text

            #Sin embargo, lo que se quiere obtener es el valor numérico de dicha clase, entonces usamos el diccionario que creamos al inicio
            etiq_ide=etiquetas.get(etiq)

            #Obtenemos el ancho y alto de cada imagen
            width=int(elem_root.find('size').find('width').text)
            height=int(elem_root.find('size').find('height').text)

            #Obtenemos, ahora, las posiciones de los bordes donde se encuentran los objetos en las imágenes
            #Para ello, nos situamos dentro de "bndbox", que a su vez se encuentra dentro de "object"
            box=elem.find('bndbox')

            #Procedemos a obtener las posiciones correspondientes y se divide, pues se hizo un resize de la imagen
            xmin=int(int(box.find('xmin').text)/(width/224))
            ymin=int(int(box.find('ymin').text)/(height/224))
            xmax=int(int(box.find('xmax').text)/(width/224))
            ymax=int(int(box.find('ymax').text)/(height/224))

            #Ahora, guardamos cada uno de los datos en las listas "imagenes","targets", en donde mencionamos que serían almacenados
            targets.append([xmin,ymin,xmax,ymax])
            imagenes.append(img)
            clase.append(etiq_ide)

    return np.array(imagenes),np.array(targets),np.array(clase)

#Ya que se crearon las funciones que nos ayudarán con la lectura de los datos, cargamos las rutas donde se
#encuentran los datos de train y test para mandar a llamar a cada una de las funciones
train_path= "C:/Users/DIANA/PyCharm/INTENTO/train"
test_path= "C:/Users/DIANA/PyCharm/INTENTO/test"

#Ahora sí, se manda a llamar a las funciones para que operen sobre cada una de los archivos e imágenes
x_train,y_train,ytrain_clase=Data(train_path)

x_test,y_test,ytest_clase=Data(test_path)
#Notar lo que valores de los píxeles aún están entre 0-255 (la normalización se hará en la capa de entrada de la red)

#Ya que la data está preprocesada, se procederá a crear la arquitectura de la red
#Debido a que la detección de objetos necesita de clasificación y regresión para obtener los bounding boxes, se creará, primero,
#la arquitectura compartida

data_input=(224,224,3) #Pues las imágenes son de esa dimensión
input_layer=tensorflow.keras.layers.Input(data_input) #Esta es la capa de entrada

#Se crean, ahora, las capas bases
#La primera capa se encargará de realizar la normalización y luego las capas para la extracción de características
capas_base=layers.Rescaling(scale=1./255,name="capa_base1")(input_layer)
capas_base=layers.Conv2D(32,3,padding="same",activation="relu",name="capa_base2")(capas_base)
capas_base=layers.MaxPooling2D(name="capa_base3")(capas_base)
capas_base=layers.BatchNormalization()(capas_base)
capas_base=layers.Conv2D(32,3,padding="same",activation="relu",name="capa_base4")(capas_base)
capas_base=layers.BatchNormalization()(capas_base)
capas_base=layers.Conv2D(32,3,padding="same",activation="relu")(capas_base)
capas_base=layers.MaxPooling2D(name="capa_base5")(capas_base)
capas_base=layers.BatchNormalization()(capas_base)
capas_base=layers.Conv2D(32,3,padding="same",activation="relu",name="capa_base6")(capas_base)
capas_base=layers.MaxPooling2D(name="capa_base7")(capas_base)
capas_base=layers.BatchNormalization()(capas_base)
capas_base=layers.Conv2D(32,3,padding="same",activation="relu",name="capa_base8")(capas_base)
capas_base=layers.MaxPooling2D(name="capa_base9")(capas_base)
capas_base=layers.Flatten(name="capa_base10")(capas_base) #La capa de entrada a la red full connected (acá se obtienen vectores)

#Ahora, a partir de la capa de Flatten, se crearán las capas para la clasificación
clasificacion=layers.Dense(128,activation="relu",name="c_clas1")(capas_base)
clasificacion=layers.Dense(10,name="cl_head")(clasificacion) #10 neuronas, pues son 10 clases

#Ahora, se definen las capas para predecir los bounding boxes a partir de la capa de flatten (igual que el paso anterior)
boundingb=layers.Dense(128,activation="relu",name="c_boundb1")(capas_base)
boundingb=layers.Dense(64,activation="relu",name="c_boundb2")(boundingb)
boundingb=layers.Dense(32,activation="relu",name="c_bound3")(boundingb)
boundingb=layers.Dense(4,activation="linear",name="bb_head")(boundingb) #4 neuronas que representan a los bounding boxes


#Finalmente, se creará el modelo final con las 2 capas de salida (clasificación y bounding boxes)
#Para ello, se deben 'unir' ambas ramas.
modelo=tensorflow.keras.Model(input_layer,
                              outputs=[clasificacion,boundingb])

#Vemos la arquitectura del modelo
modelo.summary()

#Debido a que la red fue creada para dar como resultado 2 outputs, es necesario definir dos funciones de pérdida
#para cada una de las ramas. Se usará "Sparse Categorical Crossentropy" para la clasificación, y "Mean Squared Error"
#para los bounding. Se definirán en un diccionario (tiene que coincidir el head de las últimas capas)
func_perd={"cl_head":tensorflow.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
           "bb_head":tensorflow.keras.losses.MeanSquaredError()}

#Se define el optimizador. En este caso, se usará "Adam"
modelo.compile(loss=func_perd,optimizer="Adam",
               metrics={"cl_head":"accuracy",
                        "bb_head":tensorflow.keras.metrics.MeanSquaredError()})

#Primero, se crearán dos diccionarios, para almacenar los targets individuales (bounding boxes, y clases)
train_targets={
    "cl_head":ytrain_clase,
    "bb_head":y_train
}
test_targets={
    "cl_head":ytest_clase,
    "bb_head":y_test
}


#Ahora, se procederá al entrenamiento del modelo. El número de épocas será 20 (aunque puede ser más, para mayor entrenamiento)
#pero debido al tiempo que se demora para entrenar, se colocarán solo 20 épocas. El tamaño del batch será 4
modelo.fit(x_train,train_targets,
                validation_data=(x_test,test_targets),
                batch_size=4,
                epochs=2,
                shuffle=True,
                verbose=1)
print("Se terminó de entrenar")


#Se realiza la predicción con algunos datos
ejemplos=[3,13,20,6]
ejemplos_a_predecir=[]

#Se generan las gráficas para algunas imágenes y comprobar los valores predichos por el modelo
import matplotlib.pyplot as plt #La librería matplotlib para mostrar las imágenes
for ejm in ejemplos:
  #Se genera la gráfica para cada imagen
  img=x_test[ejm]
  plt.imshow(img)
  plt.show()
  #Se agregan las imágenes a la lista de "ejemplos_a_predecir"
  ejemplos_a_predecir.append(x_test[ejm])

#Se realiza la conversión a un arreglo de Numpy
ejemplos_a_predecir=np.array(ejemplos_a_predecir)

#Se generan las predicciones para cada imagen
predicciones = modelo.predict(ejemplos_a_predecir)
print("predicciones:",predicciones)

#Se usa la función argmax para obtener la clase solo con mayor probabilidad de ser
clases=np.argmax(predicciones[0], axis = 1)
print(clases)
print("Diccionario:",etiquetas) #Se imprime el diccionario para ver qué clase fue la que predijo el modelo
