from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import json
from flask import Flask, request, Response 
import numpy as np
from PIL import Image

# load the model
model = VGG16()
app = Flask(__name__)

def predict(image):
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    labels = decode_predictions(yhat)
    label = labels[0][0]
    return label

img = load_img('./resources/mug.jpg', target_size=(224, 224))
predict(img)
@app.route('/api/predict', methods=['POST'])
def predict_route():
    img_data = request.files['file']
    img = Image.open(img_data)
    img = img.resize((224, 224), Image.ANTIALIAS)
    prediction = predict(img)
    return Response(response=json.dumps({"label": prediction[1], "confidence": float(prediction[2])}), status=200, mimetype="application/json")

@app.route('/api', methods=['GET'])
def root():
    print('GET /')
    return Response(response='', status=200)

try:
    # start flask app
    app.run(host="0.0.0.0", port=5000)
except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
