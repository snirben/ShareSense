#from ossaudiodev import error
import tensorflow as tf
from keras.preprocessing import image
import cv2
import numpy as np
import base64
from datetime import datetime
import sys
from cv2 import cv2
import requests

model_path = 'model.h5'
model = tf.keras.models.load_model(model_path)


def predict(data):
    predictions = []
    for i in data['img']:
        decoded = base64.b64decode(i['base_64_content'])
        nparr = np.fromstring(decoded, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (224, 224))
        img = image.img_to_array(img)
        img_array = np.expand_dims(img, axis=0) / 255
        probabilities = model.predict(img_array)[0]
        pred = np.argmax(probabilities)
        prediction = {'label': str(int(pred)),
                      'score': float(probabilities[pred])}
        predictions.append(prediction)
    return prediction


def send_image(encoded_string):
    request_dict = {'img': [{'name': 'stream', 'base_64_content': encoded_string}]}
    data = predict(request_dict)
    return data

import os
def main_loop(cam_ip="http://192.168.1.130:8080/shot.jpg", show_window=False):
    cam_url= 'http://' + cam_ip + ':8080/shot.jpg'
    try:
        for i in range(10):
            print(i)
            fire = False
            #response = os.system("ping " + cam_ip)

            # and then check the response...
            # if response == 0:
            #     print('up')
            # else:
            #     raise
            img_resp = requests.get(cam_url)
            encoded = base64.b64encode(img_resp.content).decode("utf-8")
            pred = None
            # Send Prediction
            pred = send_image(encoded)
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            if pred is not None:
                fire = True if pred['label'] == '0' else False
            if fire and show_window:
                cv2.rectangle(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 100)
                cv2.putText(img, 'FIRE!', (100, 250), color=(0, 0, 255), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=8,
                            thickness=8)
            if show_window:
                cv2.imshow('Phone', img)
                if cv2.waitKey(1) == 27:
                    sys.exit(0)
            if fire:
                return True
        return False
    except BaseException as err:
        print(f"Unexpected {err}")
        return False


if __name__ == '__main__':
    while True:
        main_loop(show_window=True)
