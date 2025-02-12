#!/usr/bin/python3
"""Starts a Flask web application that displays cities by states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display an HTML page listing all states and their cities"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
