#!/usr/bin/env python3
"""API Routes for Authentication Service"""
from auth import Auth
from flask import (Flask, jsonify,
                   request, abort,
                   redirect)

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def Base_route() -> str:
    """ Base route API """
    msg = {"message": "Bienvenue"}
    return jsonify(msg)

@app.route('/users', methods=['POST'])
def register_user() -> str:
    """Registers users in DB"""
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return jsonify(msg)

@app.route('/sessions', methods=['POST'])
def log_in() -> str:
    """ User login functionality """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    msg = {"email": email, "message": "logged in"}
    response = jsonify(msg)

    response.set_cookie("session_id", session_id)

    return response

@app.route('/sessions', methods=['DELETE'])
def log_out() -> str:
    """ Finds a user session and logout
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect('/')
