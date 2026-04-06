# Day - libraries & Numpy

import numpy as np

# Basic Numpy arrays
print("--- Robot Sensor Reading ---")
distance = np.array([45, 89, 23, 67, 34, 91, 12])
print(f"All Readings: {distance}")
print(f"Minimum Distance: {np.min(distance)}cm")
print(f"Maximum Distance: {np.max(distance)}cm")
print(f"Average Distance: {np.mean(distance):.2f}cm")


# Robot Position
print("\n--- Robot Position ---")
position = np.array([10, 20])  
movement = np.array([5, 3])
new_position = position + movement
print(f"Starting position: {position}")
print(f"Movement: {movement}")
print(f"New Position: {new_position}")


# Battery Readingd Over Time
print("\n--- Battery Analysis ---")
battery_readings = np.array([100, 85, 70, 55, 40, 25])
print(f"Battery Readings: {battery_readings}")
print(f"Average BAttery: {np.mean(battery_readings):.2f}%")
print(f"Battery dropped by: {battery_readings[0] - battery_readings[-1]}%")


# Speed Calculations
print("\n--- Speed Analysis ---")
speeds = np.array([2.5, 5.0, 7.5, 10.0, 8.0, 6.0])
print(f"Speeds: {speeds} m/s")
print(f"Max speed: {np.max(speeds)} m/s")
print(f"Average speed: {np.mean(speeds):.2f} m/s")