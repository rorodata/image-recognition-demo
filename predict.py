from PIL import Image
import requests
import image_pred
import json
import base64
import io

def read_image(image_spec):
    if not isinstance(image_spec, dict):
        return None
    if 'data' in image_spec:
        data = base64.b64decode(image_spec['data'])
    elif 'url' in image_spec:
        data = requests.get(image_spec['url']).content
    else:
        return None
    return Image.open(fp=io.BytesIO(data))

def predict(image, n=5):
    img = read_image(image)
    return image_pred.predict(img, n)
