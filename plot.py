#!/usr/bin/env python3

import matplotlib.pyplot as plt
from datetime import datetime

# Read data from the log file
timestamps = []
apm_values = []

with open('log_of_apm.txt', 'r') as file:
    #next(file)  # Skip header line
    for line in file:
        parts = line.strip().split(',')
        timestamp_str, apm_str = parts[0], parts[1]
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        apm = int(apm_str.split(':')[1])
        apm = min(apm, 200)
        timestamps.append(timestamp)
        apm_values.append(apm)

# Plot the data
plt.plot(timestamps, apm_values, label='APM')
plt.xlabel('Time')
plt.ylabel('APM')
plt.title('APM over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

