#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    all_states = storage.all(State).values()
    sort_states = sorted(all_states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sort_states)


@app.teardown_appcontext
def close(self):
    """This method close the current session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
