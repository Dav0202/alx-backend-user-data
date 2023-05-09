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
