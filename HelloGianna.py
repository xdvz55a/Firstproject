import subprocess
import os
import datetime
import requests
import json
import time
from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug import secure_filename

app = Flask(__name__)
api = Api(app)

now = datetime.datetime.now()
# print (now)
today = now.strftime("%Y-%m-%d-%H-%M")

@app.route('/hello/', methods=['GET'])
def upload_file():
    return 'Hello Gianna Bananna'

if __name__ == '__main__':
     app.run(host='0.0.0.0',port='5004')
