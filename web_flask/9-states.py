#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def display_states():
    """
    Rendern a template that displays a list of states.
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("9-states.html", states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def display_state_cities(id):
    """
    Render a template that displays a list of cities by state.
    """
    state = storage.get("State", id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template("9-states.html", state=state, cities=cities)
    else:
        return render_template("9-states.html", not_found=True)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
