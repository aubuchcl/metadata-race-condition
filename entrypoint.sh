#!/bin/sh

# Define the output directory
OUTPUT_DIR="/root/temp/data"

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

    TIMESTAMP=$(date +%Y%m%d%H%M%S%N)
    OUTPUT_FILE="$OUTPUT_DIR/output_$TIMESTAMP.json"
    
    cat /var/run/cycle/metadata/environment.json > "$OUTPUT_FILE"
    sleep "$interval"
done

python compare.py

# After execution, run the normal startup command
exec "$@"