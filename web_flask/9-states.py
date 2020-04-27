#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def cities_list(id='0'):
    all_states = storage.all(State).values()
    sort_states = sorted(all_states, key=lambda state: state.name)
    all_cities = storage.all(City).values()
    sort_cities = sorted(all_cities, key=lambda city: city.name)
    return render_template('9-states.html',
                           states=sort_states, cities=sort_cities, id=id)


@app.teardown_appcontext
def close(self):
    """This method close the current session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
