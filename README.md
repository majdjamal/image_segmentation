# Image Segmentation with K-Means

This experiment is about image segmentation experiments with K-Means. All models and experiments are written from scratch, using mainly NumPy and SciPy.

### K-Means
K-Means is an algorithm that partitions data into clusters. We start with (1) initializing centroids, (2) create clusters by assigning data points to the nearest centroid, and (3) move centroids towards the center of the clusters. See figure 1 for a demonstration. More about K-Means is found [here](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html).

<img src="https://media.giphy.com/media/CyOmhXxHgIHzm9pZJT/giphy.gif" width="470" height="350">
(Figure 1. A demonstration of K-Means Algorithm.)


## Image Segmentation

K-Means Clustering is used in Computer Vision for image segmentation. The goal is to represent images in formats that are easier to analyze, e.g., for edge detection.  Experimentations in this repository will use two images downloaded from Google, one of oranges, and the other of humans walking.

### Oranges
An image of oranges is used for segmentation, as seen in Figure 2. The result is shown in Figure 3.

<img src="https://i.ibb.co/RB1mpZR/orange.jpg" width="300" height="250">

(Figure 2. Image of oranges that are used for the segmentation)

<img src="https://i.ibb.co/VVf5hnd/Ska-rmavbild-2021-03-28-kl-13-18-10.png" width="470" height="250">

(Figure 3. Oranges segmented with (A) 2 clusters, and (B) 3 clusters)

### Humans walking
We can use K-Means to locate humans that are walking. The original image is shown in Figure 4, and the result of using 2 clusters is shown in Figure 5.

<img src="https://i.ibb.co/2dyYD8w/walking.jpg" width="400" height="300">

(Figure 4. Image of humans walking)

<img src="https://i.ibb.co/Th1j0qJ/walking-k2.png" width="470" height="350">

(Figure 5. Image of humans walking segmented using 2 clusters.)

## Testing

Required packages: NumPy, SciPy, cv2, and Matplotlib

Test K-Means by navigating to the directory in your terminal and type,

```bash
python experiment.py
```

Run the image segmentation experiment by typing,

```bash
python image_segmentation.py
```
