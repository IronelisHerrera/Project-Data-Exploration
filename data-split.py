
import os, os.path
import splitfolders as split
import matplotlib

input_folder = 'dataset-images/'

split.ratio(input_folder, output='output',seed=1337, ratio=(0.7,0.2,0.1), group_prefix=None)

#Anotaciones de la división de la información:

# training = conjunto de datos para el entrenamiento del modelo.

# validation = Es utilizado  para  validar  o  comprobar  nuestro modelo  durante  el  entrenamiento. Mediante las  validaciones  
#podemos  elegir  el  mejor  modelo  a  utilizar mediante los resultados de precisión arrojados en este conjunto. Igualmente determina si es necesario
#utilizar optimizadores y ajuste o 'tunning'

#testing = Para medir qué tan bueno es el modelo, para medir  el desempeño el  modelo.