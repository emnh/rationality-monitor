#!/usr/bin/env python3

from datetime import datetime, timedelta
from collections import defaultdict

# Read data from the log file
timestamps = []
apm_values = []

with open('log_of_apm.txt', 'r') as file:
    next(file)  # Skip header line
    errcount = 0
    for line in file:
        parts = line.strip().split(',')
        timestamp_str, apm_str = parts[0], parts[1]
        try:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            apm = int(apm_str.split(':')[1])
            timestamps.append(timestamp)
            apm_values.append(apm)
        except:
            errcount += 1
    print("errcount", errcount)

# Create a dictionary to store hourly average APM
hourly_average_apm = defaultdict(list)
for timestamp, apm in zip(timestamps, apm_values):
    #hour_key = timestamp.replace(minute=0, second=0, microsecond=0)
    hour_key = timestamp.replace(second=0, microsecond=0)
    hourly_average_apm[hour_key].append(apm)

# Calculate average APM per hour
for hour, values in hourly_average_apm.items():
    hourly_average_apm[hour] = sum(values) / len(values)

# Count the number of hours per day with average APM over 10
hours_over_10_per_day = defaultdict(int)
for hour, average_apm in hourly_average_apm.items():
    if average_apm > 10:
        hours_over_10_per_day[hour.date()] += 1

# Print the results
csum = 0
days = 0
for date, count in hours_over_10_per_day.items():
    print(f"{date}: {count} minutes with average APM over 10")
    csum += count
    days += 1
cavg = csum / days / 60.0
print(f"Average productivity: {cavg} hours per day over {days}")
