# CNN_Image_Classification
This program uses a Convolutional Neural Net to classify images from a data set of ...

# Convolutional Neural Network Explained
A CNNs overall objective is to extract high level features (such as edges) from an input image and based on it's training model classify this image correctly.

### Pre-Process
1. Before the feature extraction phase the data first has to be pre-processed in order to reduce computation time
  - This is key since an input image may have a high resolution and preforming a convolutional matrix operation on an 8k image can be costly
    - for this project the dataset uses only low resolution input images but same logic still applies
2. The input image has a convolution layer (kernal filter) applied to it in order to reduce image resolution and only keep key features
  - our kernel filter iterates through each pixel on the input image and performs a matrix multiplication
  ![Matrix Multiplication](https://miro.medium.com/max/500/1*GcI7G-JLAQiEoCON7xFbhg.gif)
  - during this process high level features our being extracted 
4.
