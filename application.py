import subprocess
import os
import datetime
import requests
import json
import time
from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug import secure_filename

application = Flask(__name__)
api = Api(application)

now = datetime.datetime.now()
# print (now)
today = now.strftime("%Y-%m-%d-%H-%M")

@application.route('/hello/', methods=['GET'])
def upload_file():
    return 'Hello Gianna Bananna, how are you, on Wedensday?'

if __name__ == '__main__':
    application.run()
