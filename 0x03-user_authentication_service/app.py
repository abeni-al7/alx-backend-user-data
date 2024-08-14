#!/usr/bin/env python3
"""A module for a flask app"""
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """The index of the API"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
