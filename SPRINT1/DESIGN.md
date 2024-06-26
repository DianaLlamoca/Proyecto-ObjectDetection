# DETALLES DEL DISEÑO Y ARQUITECTURA
El diseño y arquitectura de la red neuronal convolucional consta de 'capas base', las cuales consisten en capas convolucionales, que se encargarán de aplicar filtros (kernels) de diferentes tamaños, con el objetivo de extraer las características de las imágenes y la red pueda entrenarse. Estas 'capas base' serán compartidas, tanto para realizarse la clasificación, como para la predicción de las coordenadas de los *bounding boxes*. Así, la red neuronal convolucional tendrá 2 'ramas', y, por tanto, dos *outputs*: una rama encargada a realizar la clasificación y la otra se encargará de la tarea de regresión para las coordenadas de los cuadros delimitadores de los objetos en las imágenes. 
## DISEÑO:
Se aplicaron capas de filtros (capas de convolución) con un kernel de 3 (a cada capa de convolución se le aplicó el *padding*, de tal forma que cuando se apliquen cada uno de los filtros a las imágenes, la matriz resultante no se reduzca en forma, es decir, tenga el mismo *shape* que la matriz de entrada).
Por otro lado, también se usó capas de MaxPooling, las cuales se encargarán de extraer los píxeles con 'mayor relevancia' (píxeles de mayor valor en la matriz de salida) luego de haber aplicado los filtros a cada una de las imágenes en las capas de convolución; de esta forma, la matriz se hace más pequeña y, de esta manera, más eficiente serán las operaciones para las próximas capas, puesto que el *shape* de la matriz de entrada se va reduciendo.

Además, también se tuvo en cuenta las capas de 'normalización' (*batch normalization*) que se encargarán de 'centrar' y 'normalizar' cada mini-batch que llega a la red, añadiendo el hecho de que también introduce cierto ruido que actúa como regularización y así prevenir el *overfitting*.
Una vez que se hayan realizado cada una de las operaciones anteriormente descritas, la red neuronal convolucional debe tener una arquitectura lineal al final, las cuales se encargarán de realizar, en este caso, de la clasificación (para las imágenes) y la regresión (para los *bounding boxes*).

## ARQUITECTURA:

**-Capas de convolución**: 5 capas de convolución con kernel de 3 (a cada una se le aplica el *padding*)

**-Capas de MaxPooling**: Luego de cada capa de convolución, se le aplica la capa de MaxPooling --> 5 capas de MaxPooling.

**-Capas de BatchNormalization**: 4 capas de BatchNormalization

**-Capas lineales**:
- 2 capas densas (lineales) para la clasificación.
- 4 capas densas (lineales) para la regresión.
