#=================================================
# Day 10: Modules & Packages
# Robotic Journey - ROS2 Preparation
#=================================================

# 1. Importing the module from my folder 
import robot_utils                      # import the whole module

# 2. Import SPECIFIC things from a module 
from robot_utils import calculate_distance, ROBOT_VERSION

# 3. Import BUILT-IN python modules
import math
import os
import random
from datetime import datetime

print("=" * 45)
print(" Day 10: Modules & Packages")
print("=" * 45)

# Using modules
print("\n--- Custom Module (robot_utils) ---")
robot_utils.greet_robot("Alpha")
robot_utils.greet_robot("Beta")

battery = 35
status = robot_utils.battery_status(battery)
print(f"battery: {battery}% Status: {status}")

print(f"Robot Version: {ROBOT_VERSION}")

# Using specific import
print("\n --- Specific Import ---")
distance = calculate_distance(1.5, 10)     # speed = 1.5 m/s, time = 10s
print(f"Distance Travelled: {distance} meters")

# Using built-in math module
print("\n math module")
print(f"Pi Value            : {math.pi:.4f}")
print(f"Square Root 144     : {math.sqrt(144)}")
print(f"Ceiling of 4.3      : {math.ceil(4.3)}")

# Using OS Module
print("\n ---- OS module ----")
print(f"Current Folder : {os.getcwd()}")
print(f"Python Version : {os.name}")

# Using Random Module
print("\n ---- Random Module ----")
sensor_reading = round(random.uniform(0.5, 5.0), 2)
print(f"Simulated LIDAR reading : {sensor_reading} m")

# Using Datetime Module
print("\n ---- datetime module ----")
now = datetime.now()
print(f"Program ran at: {now.strftime('%Y-%m-5d %H:%M:%S')}")



