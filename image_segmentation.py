
__author__ = "Majd Jamal"

import numpy as np
import matplotlib.pyplot as plt
from kmeans import KMeans
import cv2

#=-=-=-=-=-=-=-=-=-=-
#   Image Segm.
#=-=-=-=-=-=-=-=-=-=-

image = cv2.imread('image/orange.jpg')  #Read image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Convert to RGB

X = image.reshape((-1,3))   #Reshape to (Npts, Ndim = 3)
X = np.float32(X)

#monkey
#init_positions = np.array([[144,238,144],[211,211,211]])

#orange
#o = np.array([[255,165,0], [206,152,134]])
# Two clusters with random initialization
k = 2
km = KMeans(n_clus = k)
km.fit(X)
centers = km.getCentroids()
clusters = km.getClusters()

segmented_image = centers[clusters]

segmented_image = segmented_image.reshape((image.shape))


plt.imshow((segmented_image).astype(np.uint8))
plt.xlabel('k = ' + str(k))
plt.tick_params(labelleft=False, labelbottom=False, labelright=False, labeltop=False)
plt.show()
