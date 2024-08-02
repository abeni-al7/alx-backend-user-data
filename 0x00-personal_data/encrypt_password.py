#!/usr/bin/env python3
"""Password related module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a hashed version of password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed
