import numpy as np
import sys, json
import keras
import imagenet_labels 
import scipy.misc
import matplotlib
import matplotlib.pyplot as plt


#vgg16=keras.applications.vgg16.VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None)

# b=plt.imread('/data/animal1.jpg')

# plt.imshow(b)

def topk(pred, k=3):
    topk=list(pred.argsort()[:,-k:].squeeze())
    topk.reverse()
    return topk

_model = None

def load_model():
    global _model
    if _model is None:
        _model = keras.applications.vgg16.VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None)
    return _model

def predict(image, npreds=5):
    """
    input - takes an RGB image (numpy array ) as input, preferably bigger than 224X224
    returns - json file with two lists: Label, Probability
    """
    img=scipy.misc.imresize(image, (224,224))
    vgg16=load_model()
    pred=vgg16.predict(img.reshape(1,224,224,3))
    top_npreds=topk(pred,k=npreds)
#     for i in top5:
#         print(pred[0,i], imagenet_labels.imgnet1000[i])
    labelz=[imagenet_labels.imgnet1000[i] for i in top_npreds]
    probz=[float(round(pred[0,i],2)) for i in top_npreds]
    d={"labels":labelz, "probs":probz}
    return json.dumps(d)

if __name__=='__main__':
    image=plt.imread(sys.argv[1])
    result = predict(image)
    print(result)
