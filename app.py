from flask import Flask
from flask import request

import xmltodict

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def ping():
    return 'hello'


@app.route("/feed", methods=['GET', 'POST'])
def feed():
    if request.method == 'POST':
        data = xmltodict.parse(request.data)
        print(data)
        return request.data
    else:
        return request.args.get('hub.challenge')
