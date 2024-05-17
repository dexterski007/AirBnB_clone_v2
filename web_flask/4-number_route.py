#!/usr/bin/python3
""" first route using flask """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ hello world"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """ hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ c + fun"""
    return f'C {text.replace("_"," ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """ python is cool"""
    return f'Python {text.replace("_"," ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def isnum(n):
    """ numbers are cool"""
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
