# -*- coding: utf-8 -*-
"""CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OI7ZAFaud0oJsBi9i8JSz3BK6klkeNa6

# Load Data
"""

from keras.datasets import mnist
(train_X, train_Y), (test_X,test_Y) = mnist.load_data(path='mnist.npz')

"""# Analyze Data"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from keras.utils import to_categorical
import matplotlib.pyplot as plt

# %matplotlib inline

print('Training data shape: ', train_X.shape, train_Y.shape)

print('Testing data shape: ', test_X.shape, test_Y.shape)

# find the unique numbers from the train labels
classes = np.unique(train_Y)
nClasses = len(classes)
print('Total number of outputs: ', nClasses)
print('Output classes: ', classes)

plt.figure(figsize=[5,5])

pos = 0 #for selecting the element to look at

# display what the first image in training set
plt.subplot(121)
plt.imshow(train_X[pos,:,:], cmap='gray')
plt.title("Ground Truth:  {}".format(train_Y[pos]))  #this is the class label

# display what the first image in testing set
plt.subplot(122)
plt.imshow(test_X[pos,:,:], cmap='gray')
plt.title("Ground Truth:  {}".format(test_Y[pos]))

"""# Data Pre-Process

"""

train_X = train_X.reshape(-1, 28, 28, 1)
test_X = test_X.reshape(-1, 28, 28, 1)
train_X.shape, test_X.shape

train_X = train_X.astype('float32')
test_X = test_X.astype('float32')
train_X = train_X / 255.
test_X = test_X / 255.

"""Convert the class labels to ont-hot encoding. This is the only way for a ML algorithm to interperate categorical data (by representing each category as a boolean value)

ex: Category 9 = [ 0 0 0 0 0 0 0 0 1 0]
"""

train_Y_one_hot = to_categorical(train_Y) # categorical to one hot
test_Y_one_hot = to_categorical(test_Y)

# display change for category label
print('Original label: ', train_Y[0])
print('After conversion to one-hot: ', train_Y_one_hot[0])

"""**Important** to do this next step: for model to generalize well, partition training data so ~80% is for training and the remaining 20% is validated

This will also help to reduce overfitting 
"""

from sklearn.model_selection import train_test_split
train_X, valid_X, train_label, valid_label = train_test_split(train_X, train_Y_one_hot, test_size=0.2, random_state=13)

# test the shape of the training and validation set
train_X.shape, valid_X.shape, train_label.shape, valid_label.shape

"""# Convolution Network

data will be fed through 3 convolutional layers:

1. 32 3x3 filters
2. 64 3x3 filters
3. 128 3x3 filters

After each filter the data will go through 3 max-pooling layers each the size of 2x2
"""

import keras
from keras.models import Sequential,Input,Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU

"""batch size can be expanded to 128 or 256 if memory is available. Higher batch size = higher prediction accuracy"""

batch_size = 64
epochs = 20
num_classes = 10

"""**Remember** LeakyReLu is more effective than the sigmoid function for CNNs.

## Model Data Process

"""

number_model = Sequential()
number_model.add(Conv2D(32, kernel_size=(3,3), activation='linear', input_shape=(28,28,1), padding='same'))
number_model.add(LeakyReLU(alpha=0.1))
number_model.add(MaxPooling2D((2,2), padding='same'))
number_model.add(Dropout(0.25))
number_model.add(Conv2D(64, (3,3), activation='linear', padding='same'))
number_model.add(LeakyReLU(alpha=0.1))
number_model.add(MaxPooling2D(pool_size=(2,2), padding='same'))
number_model.add(Dropout(0.25))
number_model.add(Conv2D(128, (3,3), activation='linear', padding='same'))
number_model.add(LeakyReLU(alpha=0.1))
number_model.add(MaxPooling2D(pool_size=(2,2), padding='same'))
number_model.add(Dropout(0.4))
number_model.add(Flatten())
number_model.add(Dense(128, activation='linear'))
number_model.add(LeakyReLU(alpha=0.1))
number_model.add(Dropout(0.3))
number_model.add(Dense(num_classes, activation='softmax'))

"""compile the model"""

number_model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])

# visualize the layers
number_model.summary()

"""## Train Model"""

number_train = number_model.fit(train_X, train_label, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(valid_X, valid_label))

"""## Evaluate Model"""

test_eval = number_model.evaluate(test_X, test_Y_one_hot, verbose=0)

print('Test loss: ', test_eval[0])
print('Test accuracy: ', test_eval[1])

""" ## Loss and Accuracy Plots"""

accuracy = number_train.history['accuracy']
val_accuracy = number_train.history['val_accuracy']
loss = number_train.history['loss']
val_loss = number_train.history['val_loss']
epochs = range(len(accuracy))
plt.plot(epochs, accuracy, 'bo', label='Training accuracy')
plt.plot(epochs, val_accuracy, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()

"""## Save Model"""

# Save the entire model as a SavedModel.
number_model.save('saved_model/cnn_number_model.h5py')

"""# Predict Labels"""

predicted_classes = number_model.predict(test_X)

# equate one hot encoding to actual number of class
predicted_classes = np.argmax(np.round(predicted_classes), axis=1)

predicted_classes.shape, test_Y.shape

"""print out the number of correct predictions and show a sample set of them"""

correct = np.where(predicted_classes==test_Y)[0]
print("Found {} correct labels".format(len(correct)))

for i, correct in enumerate(correct[:9]):
  plt.subplot(3,3,i+1)
  plt.imshow(test_X[correct].reshape(28,28), cmap='gray', interpolation='none')
  plt.title("Predicted {}, Class {}".format(predicted_classes[correct], test_Y[correct]))
  plt.tight_layout()

"""print out the number of incorrect predictions and show a sample set

"""

incorrect = np.where(predicted_classes!=test_Y)[0]
print("Found {} incorrect labels".format(len(incorrect)))

for i, incorrect in enumerate(incorrect[:9]):
  plt.subplot(3,3,i+1)
  plt.imshow(test_X[incorrect].reshape(28,28), cmap='gray', interpolation='none')
  plt.title("Predicted {}, Class {}".format(predicted_classes[incorrect], test_Y[incorrect]))
  plt.tight_layout()

"""## Classification Report
The aim here is to identify which labels are misclassified the most.
"""

from sklearn.metrics import classification_report
target_names = ["Class {}".format(i) for i in range(num_classes)]
print(classification_report(test_Y, predicted_classes, target_names=target_names))