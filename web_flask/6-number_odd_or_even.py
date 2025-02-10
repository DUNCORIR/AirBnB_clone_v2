#!/usr/bin/python3
"""Flask web application to display odd or even numbers"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns a simple greeting message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays 'C ' followed by the value of text"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Displays 'Python ' followed by the value of text"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page with 'Number: n' if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Displays an HTML page indicating if n is odd or even"""
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template(
        "6-number_odd_or_even.html", n=n, odd_or_even=odd_or_even
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
