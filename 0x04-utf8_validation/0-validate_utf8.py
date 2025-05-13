#!/usr/bin/env python3
""" UTF-8 Validation"""


def validUTF8(data) -> bool:
    """Returns True is valid UTF-8 and False when otherwise."""
    try:
        bytes(data).decode('utf-8')
        return True
    except ValueError:
        return False
