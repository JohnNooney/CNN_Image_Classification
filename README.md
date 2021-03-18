# CNN vs RNN Image Classification
This program uses a Convolutional Neural Net to classify images from a data set of ...

## Setup
 Python 3.5-3.8 is required for compatibility with all required modules
 
 ```
 # Clone this reposititory
 git clone https://github.com/JohnNooney/CNN_vs_RNN_Image_Classification
 
 # Go into repository
 cd ../cnn_vs_rnn_image_classification
 
 # Install required modules
 pip install -r requirements.txt
 ```
 
 ## Usage
 Upon launching the application with ``` python app.py ``` you will be met with a window that can allows you to draw in the black box
 
 - use the left mouse button to draw
 - 'C' to clear box
 - 'P' to predict 
  - in the console you will see the output from each models prediction
 - 'Q' to quit  

# Convolutional Neural Network Explained
A CNNs overall objective is to extract high level features (such as edges) from an input image and based on it's training model classify this image correctly.

![CNN Pipeline](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1512486717/Typical_cnn_kecdep.png)

## Intial Convolution (Feature Maps)
1. During the feature extraction phase the input image needs be rescaled in order to reduce computation time
  - This is key since an input image may have a high resolution and preforming a convolutional matrix operation on an 8k image can be costly
    - for this project the dataset uses only low resolution input images but same logic still applies
2. The input image has a convolution layer (kernal filter) applied to it in order to reduce image resolution and only keep key features
  - our kernel filter iterates through each pixel on the input image and performs a matrix multiplication
  ![Matrix Multiplication Example](https://miro.medium.com/max/500/1*GcI7G-JLAQiEoCON7xFbhg.gif)
  - during this process the high level features our being extracted into what is called 'Feature Maps'
4. In the case of RGB images, each color goes through the kernal filter, creating its own featur map, and the end result gets summed together

## Pooling (Subsampling)
The poolings main goal is to reduce computational power through **dimentionality reduction**, **noise reduction**, and **dominant features** extraction. There are 2 main types of pooling; max pooling and average pooling. Max pooling was chosen here since it has overall better performance
 - **Max Pooling**: returns the max value from the portion of the image covered
 - Average Pooling: returns the average from all the values in the portion of the image covered

In this layer the highest pixel value in a designated region (deteremined by kernel size) of the feature map is extracted. This subsample is then used to hold the key features of the image.

![Pooling Example](https://miro.medium.com/max/500/1*KQIEqhxzICU7thjaQBfPBQ.png)
 
## Classification (Fully-Connected)
This layer is when all the key features are flattened into a single dimensional vector to be processed by the Multi-layer Percepton. Our data is being fed to a Neural Network that, over many epochs, will be able to distinguish between dominating features and low-level features present in the images and classify them accordingly.

- The classification technique used here is Softmax classifier

# Recurrent Neural Network (LSTM) Explained
A RNN's main distinctive feature is the ability to persist memory through each testing cycle, otherwise known as a timestep. This gives the network the ability to connect previous information to the current task. 
 - The specific architecture used here is the Long Short Term Memory. This architecture solves the problem of long-term dependency: being able to remember information for long periods of time.

LSTM Architecture            |  Standard Architecture
:-------------------------:|:-------------------------:
![LSTM RNN](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-chain.png)  |  ![Standard RNN](https://colah.github.io/posts/2015-08-Understanding-LSTMs/img/LSTM3-SimpleRNN.png)

- The key to the LSTM is the cell state. This is the straight line that runs through the entire diagram and what is responsible for allowing data to persist through the entire training process. Only certain data is allowed into the cell state and this is regulated by sigmoid neural net layers along the line. 

## Input Sequence
Since we are dealing with images, this is an important step to consider since we won't be applying any convolutional filters. 

In order to recognize a number we will treat each row of pixels in the image as one timestep. This way the model is able to analyze one row at a time while having memory of the past rows aswell. 

# Sources
https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53 

https://www.datacamp.com/community/tutorials/convolutional-neural-networks-python 

https://colah.github.io/posts/2015-08-Understanding-LSTMs/
