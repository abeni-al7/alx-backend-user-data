#!/usr/bin/env python3
"""Basic auth implementation method"""
import base64
from api.v1.auth.auth import Auth
from typing import Union


class BasicAuth(Auth):
    """Basic Auth implementation class"""
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> Union[
                                                 str, None]:
        """Returns base64 part of authorization header"""
        if authorization_header is None:
            return None
        if not type(authorization_header) == str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decodes the base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if not type(base64_authorization_header) == str:
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            value = decoded.decode('utf-8')
            return value
        except Exception:
            return None
