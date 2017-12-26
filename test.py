import firefly
import sys

url = sys.argv[1]

api = firefly.Client("https://anand-test-1.rorocloud.io/")
predictions = api.predict(image={"url": url})
print(predictions)
