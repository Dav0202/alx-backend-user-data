#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns encrypted password """
    encoded_pass = password.encode()
    pass_word = bcrypt.hashpw(encoded_pass, bcrypt.gensalt())

    return pass_word


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Check if encrypted password is valid """
    valid = False
    encoded_pass = password.encode()
    if bcrypt.checkpw(encoded_pass, hashed_password):
        valid = True
    return valid
