import roro
import sys

DEFAULT_IMAGE_URL = "https://rorodata-tmp.s3.amazonaws.com/ring-tailed-lemur.jpg"

try:
    url = sys.argv[1]
except IndexError:
    print("No image provided, using the default image.")
    url = DEFAULT_IMAGE_URL

print("Predicting object in", url)
api = roro.Client("https://image-recognition-demo.rorocloud.io/")
predictions = api.predict(image={"url": url})
print(predictions)
