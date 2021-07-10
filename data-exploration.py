
import numpy as np
from PIL import Image
import glob, os, os.path
import splitfolders
import matplotlib

path_earphone = '../Proyecto-PrimeraEntrega/dataset-images'
path_cellphone = '../Proyecto-PrimeraEntrega/dataset-images'

au_dir = os.path.join(path_earphone, 'auriculares')
cell_dir = os.path.join(path_cellphone, 'celular')

class_names = ['auriculares', 'celular', 'laptop', 'altaboces', 'television',
               'tableta']



