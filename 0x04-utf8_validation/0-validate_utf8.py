#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Check if data is a valid UTF-8 encoding"""
    n_bytes = 0

    for num in data:
        byte = num & 0xFF  # Use only the least significant 8 bits

        if n_bytes == 0:
            if (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            elif (byte >> 7) != 0:  # Invalid single-byte (must be 0xxxxxxx)
                return False
        else:
            if (byte >> 6) != 0b10:  # Must start with 10 as continuation byte
                return False
            n_bytes -= 1

    return n_bytes == 0
