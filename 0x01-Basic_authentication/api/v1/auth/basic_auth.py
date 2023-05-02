#!/usr/bin/env python3
""" Basic Authentication Module
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Class for basic authentication """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract Base 64 Authorization Header """

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]

        return encoded

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Returns the user email and password """

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':', 1)

        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user

        return None
