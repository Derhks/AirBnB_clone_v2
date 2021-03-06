#!/usr/bin/python3
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return 'C %s' % str(escape(text)).replace('_', ' ')


@app.route('/python', strict_slashes=False)
def python_root():
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    return 'Python %s' % str(escape(text)).replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
