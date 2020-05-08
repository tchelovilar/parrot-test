import os
import random
import string
import redis
import json

from time import ctime
from flask import Flask
from flask import request


class info():
    def __init__(self):
        self.requests = 0

        self.redis_cli = None
        redis_server = os.environ.get("REDIS_SERVER")

        if redis_server:
            port = os.environ.get("REDIS_PORT", 6379)
            self.redis_cli = redis.Redis(host=redis_server, port=port)


    def request_count(self):
        self.requests += 1
        return self.requests



def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


app = Flask(__name__)

info = info()

@app.route('/health')
def health():
    return 'ok'


@app.route('/post', methods=['POST'])
def post():
    return_content = f"Content Type: {request.content_type}<br><br>Content:<br>{request.data}"
    return return_content


@app.route('/fail')
def fail():
    Exception("Force 503")


@app.route('/headers')
def headers():
    return str(request.headers).replace("\n","<br>\n")


@app.route('/')
def root():
    hostname = os.environ.get("HOSTNAME")
    date = ctime()
    string = randomString()
    request_count = info.request_count()

    if info.redis_cli:
        try:
            info.redis_cli.lpush("random-strings",string)
        except:
            pass

    return_content = f"Hostname: {hostname}<br>Date Time: {date}<br>Random String: {string}<br>Requests Total: {request_count}"
    return return_content

