import sys
import keras
import imagenet_labels
import scipy.misc

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

    def get_prediction(index):
        label = imagenet_labels.imgnet1000[index]
        proba = float(pred[0, index])
        return {
            "label": label,
            "probability": proba
        }

    predictions = [get_prediction(i) for i in top_npreds]
    return predictions

if __name__=='__main__':
    image=plt.imread(sys.argv[1])
    result = predict(image)
    print(result)
