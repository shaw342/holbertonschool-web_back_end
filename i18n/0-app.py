#!/usr/bin/env python3
"""python file handle the all route"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """routet return the templates of homepage"""
    return render_template("./index.html")


if __name__ == "__main__":
    app.run(debug=True)
