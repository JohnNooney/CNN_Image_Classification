import numpy as np
import cv2

from keras import models

class NeuralNet(object):

    def __init__(self):
        # loading model data
        self.cnn_model = models.load_model('Models/saved_model/cnn_number_model.h5py')
        self.rnn_model = models.load_model('Models/saved_model/rnn_number_model.h5py')

    def predict(self, image):
        input = cv2.resize(image, (28, 28))
        input = input.reshape((28, 28, 1))
        input = input.astype('float32') / 255.
        input = self.cnn_model.predict(np.array([input]))
        return  np.argmax(np.round(input), axis=1)

    def predict_rnn(self, image):
        input = cv2.resize(image, (28, 28))
        input = input.reshape((28, 28, 1))
        input = input.astype('float32') / 255.
        input = np.array([input]).reshape(1, 28, 28) # reshape to conform to rnn input shape
        input = self.rnn_model.predict(input)
        return np.argmax(np.round(input), axis=1)