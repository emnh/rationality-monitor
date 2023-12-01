#!/usr/bin/env python3

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta
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
        timestamps.append(timestamp)
        apm_values.append(apm)

# Create a dictionary to store hourly average APM
hourly_average_apm = defaultdict(list)
for timestamp, apm in zip(timestamps, apm_values):
    hour_key = timestamp.replace(minute=0, second=0, microsecond=0)
    hourly_average_apm[hour_key].append(apm)

# Calculate average APM per hour
for hour, values in hourly_average_apm.items():
    hourly_average_apm[hour] = sum(values) / len(values)

# Create a matrix for the heatmap
heatmap_data = []
current_date = min(hourly_average_apm.keys())
end_date = max(hourly_average_apm.keys())

while current_date <= end_date:
    row = []
    for _ in range(24):
        average_apm = hourly_average_apm.get(current_date, 0)
        row.append(average_apm)
        current_date += timedelta(hours=1)
    heatmap_data.append(row)

# Transpose the matrix to switch both axes and data
transposed_heatmap_data = np.transpose(heatmap_data)

# Reset current_date for labeling
current_date = min(hourly_average_apm.keys())

# Convert dates to string for labeling
date_labels = [current_date.strftime('%Y-%m-%d') for _ in range(24)]
current_date += timedelta(days=1)

# Plot the heatmap with switched axes and data
plt.figure(figsize=(12, 8))
sns.heatmap(transposed_heatmap_data, cmap='YlGnBu', annot=True, fmt=".1f", cbar_kws={'label': 'Average APM'},
            yticklabels=range(24), xticklabels=date_labels)
plt.xlabel('Hour of Day')
plt.ylabel('Date')
plt.title('Average APM per Hour - Calendar View (Switched Axes and Data)')
plt.tight_layout()
plt.show()

