#!/usr/bin/env python3
""" Authentication Module
"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """ Class managing authentication of API """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        len_path = len(path)
        if len_path == 0:
            return True

        slash_path = True if path[len_path - 1] == '/' else False

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for exc in excluded_paths:
            len_exc = len(exc)
            if len_exc == 0:
                continue

            if exc[len_exc - 1] != '*':
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[:len_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""

        if request is None:
            return None

        SESSION_NAME = os.getenv("SESSION_NAME")

        if SESSION_NAME is None:
            return None

        session_id = request.cookies.get(SESSION_NAME)

        return session_id
