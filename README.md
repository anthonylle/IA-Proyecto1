![Imgur](https://i.imgur.com/E8Ta3b1.png)
## INTELIGENCIA ARTIFICIAL, II SEMESTRE 2018

### Enlace de GitHub
El repositorio de este proyecto puede ser accedido mediante el [siguiente enlace](https://github.com/anthonylle/IA-Proyecto1)

### Reporte técnico
#### Módulo de pre-procesamiento de datos, normalización y codificación

#### Módulo de entrenamiento y predicción con random forests

#### Módulo de entrenamiento y predicción con redes neuronales 

#### Módulo de cross validation y evaluación genérico

### Manual de usuario
Lo primero que debe tener es:

* Python 3 (recomendable 3.6)
* Anaconda	| descargar desde [aquí](https://www.anaconda.com/download/)

Seguidamente debe crear un ambiente de Python para trabajar con el comando ```conda``` y activarlo con el subcomando ```activate```. Ejecutar lo siguiente en el terminal:

```
$ conda create -n <nombre_ambiente> python=3.6
$ conda activate <nombre_ambiente>
```
Suponiendo que el nombre del ambiente fue ```trabajo```
ahora debería indicarse en el terminal que este ambiente es el que está activo de la siguiente manera:

```
(trabajo)$ 
```
Luego se debe instalar algunas librerías con el comando ```pip```, y/o ```conda``` en caso de tener algún problema con la instalación de ```pip```.

Las librerías requeridas son:

* tensorflow
* numpy (incluida en tensorflow)
* scipy
* pandas

La que más trabajo lleva es la de tensorflow, ya que en algunos casos el paquete no es reconocido luego de su instalación. Para instalarlo con ```pip``` se utiliza:

```
pip install --ignore-installed --upgrade \ https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.11.0-py3-none-any.whl
```
Se puede verificar que esté instalado ejecutando los siguientes comandos:

```
(trabajo)$ python
>>> import tensorflow
>>> 
```
Si no da error, todo bien! en caso contrario, instalar mediante ```conda```: 

```
(trabajo)$ conda install tensorflow
```
Este instalador solicitará varias confirmaciones, y cuando termine se puede verificar que esté instalado de la misma manera que la mencionada anteriormente.
De igual manera las demás librerías se instalan fácilmente con ```pip```.

```
(trabajo)$ pip install <numpy|pandas|scipy>
```

####Para probar el programa
El archivo principal se encuentra en la raíz de la carpeta del proyecto, cuyo nombre es ```main.py```.

Se debe tener en cuenta lo siguiente:

* Este programa utiliza dos algoritmos: Random Forests y Redes Neuronales
* Para elegir alguno de los dos algoritmos, se debe proporcionar el parámetro adecuado, y además, estos requieren de otros parámetros para su correcto funcionamiento
* Para utilizar Random forests, se debe indicar mediante el parámtro: ```--arbol```
	* Además, ```--umbral-poda``` sirve para especificar la ganancia de información mínima requerida para realizar una partición. Este es un parámetro requerido.
* Para utilizar Redes neuronales, se debe indicar mediante el parámtro: ```--red-neuronal```, además:
	* ```--numero-capas``` para indicar cuántas capas tendrá la red neuronal.
	* ```--unidades-por-capa``` indica cuántas unidades por capa existirá en la red neuronal.
	* ```--funcion-activacion``` define la salida de los nodos en una Red Neuronal para un conjunto de entradas dado. Las opciones disponibles son: ```relu```, ```sigmoid```, ```softmax```, ```softplus```.

Ejemplos:

```
(trabajo)$ python main.py --arbol --umbral-poda 0.32
(trabajo)$ python main.py --red-neuronal --numero-capas 10 --unidades-por-capa 2 --funcion-activacion relu
```
La salida del programa es el error de entrenamiento y pruebas


### Distribución de nota y trabajo realizado

Estudiante| Anthony | Jake 	| Randall |
---------	|---------|---------|---------|
Tareas| 		100	| 		100	| 		100	|

