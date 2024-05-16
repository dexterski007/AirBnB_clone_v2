#!/usr/bin/python3
""" first route using flask """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ hello world"""
    return "Hello HBNB!\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
