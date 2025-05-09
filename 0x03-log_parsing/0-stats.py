#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""

import sys
import signal
import re

valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
code_counts = {}
total_size = 0
line_counter = 0

line_pattern = re.compile(
    r'^(\d{1,3}(?:\.\d{1,3}){3}) - '
    r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
    r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)


def print_stats():
    """Prints the accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(code_counts.keys(), key=int):
        print(f"{code}: {code_counts[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL+C)"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        match = line_pattern.match(line)
        if match:
            ip, s_code, file_size = match.groups()
            try:
                total_size += int(file_size)
                if s_code in valid_codes:  # status code
                    code_counts[s_code] = code_counts.get(s_code, 0) + 1
            except Exception:
                pass
        line_counter += 1
        if line_counter % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
except Exception:
    pass
finally:
    print_stats()
