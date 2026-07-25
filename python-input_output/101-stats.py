#!/usr/bin/python3
import sys

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_size = 0
line_count = 0


def print_stats():
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        try:
            parts = line.split()

            size = int(parts[-1])
            status = parts[-2]

            total_size += size

            if status in status_codes:
                status_codes[status] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue

except KeyboardInterrupt:
    pass
finally:
    print_stats()
