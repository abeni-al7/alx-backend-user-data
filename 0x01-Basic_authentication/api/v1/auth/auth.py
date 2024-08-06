#!/usr/bin/env python3
"""Authentication module"""
from flask import request
from typing import List, TypeVar, Union


class Auth:
    """Authentication class"""
    def require_auth(self, path: Union[str, None],
                     excluded_paths: List[str]) -> bool:
        """Determines if the path requires authentication"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        if request is None:
            return None
        if request.headers.get('Authorization'):
            return request.headers['Authorization']
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None"""
        return None
