import numpy as np
import keras
from PIL import Image
import scipy.misc
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import io

vgg16 = keras.applications.vgg16.VGG16(
            include_top=True,
            weights='imagenet',
            input_tensor=None,
            input_shape=None)

import requests
URL_CLASS_LABELS = "https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json"
class_labels = requests.get(URL_CLASS_LABELS).json()

def get_class_label(index):
    return class_labels[str(index)][1]

def predict_image(image):
    img=scipy.misc.imresize(image, (224,224))
    img=img-127.5 # zero centering the image pixel values gives better accuracies, as the original VGG16 model was trained so
    pred=vgg16.predict(img.reshape(1,224,224,3))

    # convert pred into a flat array
    pred = pred.reshape(-1)

    #index = pred.argmax()
    #return get_class_label(index)
    x = pred.argsort()[::-1][:3]

    return [{"label": get_class_label(i), "probability": float(pred[i])} for i in x]

def predict(image):
    img = read_image(image['url'])
    return predict_image(img)

def read_image(url):
    data = requests.get(url).content
    return Image.open(fp=io.BytesIO(data))

if __name__ == "__main__":
    import sys
    url = sys.argv[1]
    print(predict(url))
