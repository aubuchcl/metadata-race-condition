#!/bin/sh

# Define the output file
OUTPUT_FILE="/root/temp/data"

# Set the duration and interval
duration=10   # Total duration in seconds
interval=0.5  # Interval in seconds
start_time=$(date +%s)

# Loop for the specified duration
while true; do
    current_time=$(date +%s)
    elapsed_time=$((current_time - start_time))
    
    if [ "$elapsed_time" -ge "$duration" ]; then
        break
    fi

    cat /var/run/cycle/metadata/environment.json >> "$OUTPUT_FILE"
    echo "\n---\n" >> "$OUTPUT_FILE"  # Separator for readability
    sleep "$interval"
done

# After execution, run the normal startup command
exec "$@"
