#!/usr/bin/python3
import sys
import signal

# Initialize counters and accumulators
file_size_total = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    global file_size_total, status_counts
    print(f"File size: {file_size_total}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")
    print()

def handle_interrupt(signal, frame):
    print_statistics()
    sys.exit(0)

# Set up signal handler for keyboard interruption
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        
        # Check if the line matches the expected format
        parts = line.split()
        if len(parts) == 7:
            try:
                status_code = int(parts[5])
                file_size = int(parts[6])
                
                # Check if the status code is in the expected set
                if status_code in status_counts:
                    file_size_total += file_size
                    status_counts[status_code] += 1
            except ValueError:
                continue
        
        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
