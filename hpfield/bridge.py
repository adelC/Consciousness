import numpy as np

import skimage.data
from skimage.color import rgb2gray
from skimage.filters import threshold_mean
from skimage.transform import resize
import network


def preprocessing(img, w=128, h=128):
    # Resize image
    img = resize(img, (w, h), mode='reflect')

    # Thresholding
    thresh = threshold_mean(img)
    binary = img > thresh
    shift = 2*(binary*1)-1  # Boolian to int

    # Reshape
    flatten = np.reshape(shift, (w*h))
    return flatten


def train():

    # Load data
    fruit = skimage.data.shepp_logan_phantom()
    cat = rgb2gray(skimage.data.cat())
    skimage.io.imsave("fruit.png", fruit)
    skimage.io.imsave("cat.png", cat)
    # Marge data
    data = [fruit, cat]

    # Preprocessing
    print("data before preprocessing shape", data[0].shape)
    print("Start to data preprocessing...")
    data = [preprocessing(d) for d in data]

    print("data after preprocessing shape", data[0].shape)

    # Create Hopfield Network Model
    model = network.HopfieldNetwork()
    model.train_weights(data)
    return model


def retreive(img, model):
    # Generate testset
    test = [img]
    predicted = model.predict(test, threshold=0, asyn=False)
    return predicted
