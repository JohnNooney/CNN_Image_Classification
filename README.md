# CNN_Image_Classification
This program uses a Convolutional Neural Net to classify images from a data set of ...

# Convolutional Neural Network Explained
A CNNs overall objective is to extract high level features (such as edges) from an input image and based on it's training model classify this image correctly.

![CNN Pipeline](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1512486717/Typical_cnn_kecdep.png)

## Pre-Process (Feature Maps)
1. During the feature extraction phase the input image needs be rescaled in order to reduce computation time
  - This is key since an input image may have a high resolution and preforming a convolutional matrix operation on an 8k image can be costly
    - for this project the dataset uses only low resolution input images but same logic still applies
2. The input image has a convolution layer (kernal filter) applied to it in order to reduce image resolution and only keep key features
  - our kernel filter iterates through each pixel on the input image and performs a matrix multiplication
  ![Matrix Multiplication](https://miro.medium.com/max/500/1*GcI7G-JLAQiEoCON7xFbhg.gif)
  - during this process the high level features our being extracted into is called 'Feature Maps'
4. In the case of RGB images, each color goes through the kernal filter and the end result gets summed together






# Sources
https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53 

https://www.datacamp.com/community/tutorials/convolutional-neural-networks-python 
