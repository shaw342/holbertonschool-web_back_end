#!/usr/bin/env python3
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app=app)


class config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    TIMEZON = "UTC"


app.config(config)


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """routet return the templates of homepage"""
    return render_template("./index.html")


if __name__ == "__main__":
    app.run()
