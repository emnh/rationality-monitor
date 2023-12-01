#!/usr/bin/env python3

import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict

# Read data from the log file
timestamps = []
apm_values = []

with open('log_of_apm.txt', 'r') as file:
    next(file)  # Skip header line
    for line in file:
        parts = line.strip().split(',')
        timestamp_str, apm_str = parts[0], parts[1]
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        apm = int(apm_str.split(':')[1])
        #apm = min(apm, 200)
        timestamps.append(timestamp)
        apm_values.append(apm)

# Aggregate data per hour
hourly_data = defaultdict(list)
for timestamp, apm in zip(timestamps, apm_values):
    hour_key = timestamp.replace(minute=0, second=0, microsecond=0)
    hourly_data[hour_key].append(apm)

# Calculate average APM per hour
hourly_average_apm = [(hour, sum(values) / len(values)) for hour, values in hourly_data.items()]

# Separate the aggregated data into two lists for plotting
hour_labels, average_apm_values = zip(*hourly_average_apm)

# Plot the data
plt.plot(hour_labels, average_apm_values, label='Average APM per Hour', marker='o')
plt.xlabel('Time (Hourly Intervals)')
plt.ylabel('Average APM')
plt.title('Average APM per Hour')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

