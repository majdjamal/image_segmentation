# Image Segmentation with K-Means

This repository contains experiments with K-Means Clustering and image segmentation. All models and experiments are written from scratch, using mainly NumPy and SciPy.

### K-Means
K-Means is an algorithm that partitions data into clusters. We start with (1) initializing centroids, (2) create clusters by assigning data points to their nearest centroid, and (3) move centroids towards the center of the clusters. See figure 1 for a demonstration. More about K-Means is found [here](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html).

<img src="https://media.giphy.com/media/CyOmhXxHgIHzm9pZJT/giphy.gif" width="470" height="350">
(Figure 1. A demonstration of K-Means Algorithm.)


## Image Segmentation

K-Means Clustering can be used for image segmentation. The goal is to represent images in formats that are easier to analyze, e.g., for edge detection. This is also known as image processing. Experiments in this section use two images downloaded from Google, one of oranges, and one of humans walking.

### Oranges
An image of oranges is used for segmentation. The original image is shown in Figure 2, and the result in Figure 3.

<img src="https://i.ibb.co/RB1mpZR/orange.jpg" width="300" height="250">

(Figure 2. Image of oranges that are used for the segmentation)

<img src="https://i.ibb.co/VVf5hnd/Ska-rmavbild-2021-03-28-kl-13-18-10.png" width="470" height="250">

(Figure 3. Oranges segmented with (A) 2 clusters, and (B) 3 clusters)

### Humans walking
Consider the image in Figure 4. There are no clear edges because humans are walking. We can highlight these humans with image segmentation, and it becomes easier to detect edges. The segmentation result is demonstrated in Figure 5.

<img src="https://i.ibb.co/2dyYD8w/walking.jpg" width="400" height="300">

(Figure 4. Image of humans walking)

<img src="https://i.ibb.co/Th1j0qJ/walking-k2.png" width="470" height="350">

(Figure 5. Image of humans walking segmented with 2 clusters.)

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
