#!/bin/sh

# Define the output file
OUTPUT_FILE="/root/temp/data"

# Ensure the directory exists
mkdir -p "$(dirname "$OUTPUT_FILE")"

# Set the duration and interval
duration=10   # Total duration in seconds
interval=0.5  # Interval in seconds
end_time=$((SECONDS + duration))

# Loop for the specified duration
while [ $SECONDS -lt $end_time ]; do
    cat /var/run/cycle/metadata/environment.json >> "$OUTPUT_FILE"
    echo "\n---\n" >> "$OUTPUT_FILE"  # Separator for readability
    sleep "$interval"
done

# After execution, run the normal startup command
exec "$@"
