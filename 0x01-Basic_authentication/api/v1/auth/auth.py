#!/usr/bin/env python3
""" Authentication Module
"""
from flask import request


class Auth:
    """ Class managing authentication of API """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for checking if endpoint requires auth """
        return False


    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
