#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Renders a template that displays a list of cities by states.
    """
    states = sorted(storage.all("State").values(), key=lambda s: s.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda c: c.name)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
