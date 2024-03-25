#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def Ctext(text):
    txt = text.replace("_", " ")
    return "C {}".format(txt)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def PyText(text="is cool"):
    txt = text.replace("_", " ")
    return "Python {}".format(txt)


@app.route("/number/<int:n>", strict_slashes=False)
def Int_n(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def Html(n):
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_odd(n):
    return render_template("6-number_odd_or_even.py", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
