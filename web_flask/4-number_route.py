#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    return "C " + str(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
def python_route0():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    return "Python " + str(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    return n + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
