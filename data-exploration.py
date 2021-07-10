## Exploración de datos

#En esta sección, trabajararemos con las siguientes librerías: matplotlib, os, splitfolders


from os import read
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
#%%matplotlib inline

image_name = '../Proyecto-PrimeraEntrega/dataset-images/altavoces/altavoces0.jpg'

read_image = img.imread(image_name)
print(np.shape(read_image))

## IMAGE DIMENSIONS

# output: (900, 1600, 3)

plt.figure(figsize=(900,1600))
plt.imshow(read_image, cmap='hot', interpolation='nearest')
plt.axis('off')
plt.title('Altavoz')
plt.show()


# %%
