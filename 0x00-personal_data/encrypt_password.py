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
