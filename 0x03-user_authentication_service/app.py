#!/usr/bin/env python3
"""A module for a flask app"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """The index of the API"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user():
    """An endpoint for user registration"""
    email = request.form["email"]
    password = request.form["password"]
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """An endpoint for user login"""
    email = request.form["email"]
    password = request.form["password"]
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        if session_id:
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie("session_id", session_id)
            return response
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
