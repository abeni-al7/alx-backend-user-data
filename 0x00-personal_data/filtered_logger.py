#!/usr/bin/env python3
"""A module for a function that obfuscates sensitive data"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns an obfuscated version of message"""
    return re.sub(f"({'|'.join(fields)})=[^{separator}]*",
                  lambda m: f"{m.group(1)}={redaction}", message)
