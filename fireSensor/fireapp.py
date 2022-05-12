from flask import Flask, jsonify
import requests
from flask_cors import CORS
import predict
app = Flask(__name__)
CORS(app)



@app.route('/cams_check')
def cams():
    response = requests.get('http://localhost:8000/api/getcams/', {})
    flag = 0
    if response.status_code == 200:
        cams = response.json()
        for cam in cams:
            flag = 0
            result = predict.main_loop(cam_url=cam['cam_ip'] + '/shot.jpg', show_window=True)
            if result and flag == 0:
                flag = 1
                requests.post('http://localhost:8000/api/toggleFire/', {'id': cam['id']})
    if flag == 1:
        return 'True'
    return 'False'


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
