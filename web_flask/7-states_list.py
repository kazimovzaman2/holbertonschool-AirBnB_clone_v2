#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """
    Closes the database connection after each request.
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Renders a template that displays a list of states.
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
