#!/usr/bin/python3
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
