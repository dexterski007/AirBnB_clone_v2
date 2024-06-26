#!/usr/bin/python3
""" first route using flask """

from flask import Flask, render_template
from models import storage
from models.state import State


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def isnum_temp(n):
    """ numbers are cool with a template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def isnum_even(n):
    """ numbers are cool with a template even now"""
    check = ""
    if n % 2 == 0:
        check = "even"
    else:
        check = "odd"
    return render_template('6-number_odd_or_even.html', n=n, check=check)


@app.route('/states_list', strict_slashes=False)
def stateslist():
    """ dbs are not cool """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by():
    """ lets see with this task """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
def statez():
    """ lets see with this task statez """
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def statez_id(id):
    """ lets see with this task """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exception):
    """ teardown function """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
