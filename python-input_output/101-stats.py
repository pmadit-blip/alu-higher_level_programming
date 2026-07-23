#!/usr/bin/python3
"""Log statistics script."""

import sys


def print_stats(total_size, status_codes):
    """Print statistics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_codes):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


total_size = 0
line_count = 0

status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

try:
    for line in sys.stdin:
        parts = line.split()

        try:
            status = int(parts[-2])
            size = int(parts[-1])

            total_size += size

            if status in status_codes:
                status_codes[status] += 1

        except (ValueError, IndexError):
            pass

        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
