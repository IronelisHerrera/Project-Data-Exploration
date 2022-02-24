
import os, os.path
import splitfolders as split
import matplotlib

input_folder = 'dataset-images/'

split.ratio(input_folder, output='output',seed=1337, ratio=(0.80,0.10, 0.10), group_prefix=None)
