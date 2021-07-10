
import os, os.path
import splitfolders as split
import matplotlib

#os.makedirs('output')

input_folder = 'dataset-images/'

split.ratio(input_folder, output='output',seed=1337, ratio=(0.7,0.2,0.1), group_prefix=None)