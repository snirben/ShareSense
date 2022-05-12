from flask import Flask, jsonify
import requests
app = Flask(__name__)


@app.route('/cams')
def cams():
    response = requests.get('http://localhost:8000/api/getcams/', {})
    if response.status_code == 200:
        return jsonify(response.json())
    return {}


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()