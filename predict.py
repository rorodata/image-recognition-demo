import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import image_pred
import json

def predict(image_file, format="png", n=5):
    img = plt.imread(image_file, format=format)
    jsondata = image_pred.predict(img, n)
    return json.loads(jsondata)
