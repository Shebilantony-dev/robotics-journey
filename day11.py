########################################################
# Day 11 - Matplotlib - Data Visualization
########################################################

import matplotlib.pyplot as plt
import random

# PART 1 - Line Chart 
#Simulating LIDAR Sensor Readings over Time

########################################################

print("Drawing Line Chart...")

time_steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]            #Seconds
distance = [2.1, 2.4, 2.8, 3.0, 2.7, 2.3, 2.0, 1.8, 1.5, 1.2]       #meters
plt.figure(figsize=(8, 4))                                                        #Create a Canvas
plt.plot(time_steps, distance, color="blue", marker="o", linestyle="-", linewidth=2)    #draw the line
plt.title("LIDAR Distance Readings Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Distance (meters)")
plt.grid(True)                              #show grid
plt.tight_layout()                        #clean spacing
plt.savefig("day11_line_chart.png")          #save as image
plt.show()                                   #display it
print("Line Chart Saved!")

#########################################################

#PART 2 - Bar Chart
#Compare Battery levels of 3 Robots

#########################################################

print("Drawing Bar Chart... ")

robot = ["Alpha", "Beta", "Gamma"]
battery = [80, 35, 92]
colors = ["Green", "Red", "Blue"]

plt.figure(figsize=(6, 4))
plt.bar(robot, battery, color=colors)
plt.title("Robot Battery, Levels")
plt.xlabel("Robot Name")
plt.ylabel("BAttery (%)")
plt.ylim(0, 100)               #y-axis from 0 to 100
plt.tight_layout()
plt.savefig("day11_bar_chart.png")
plt.show()
print("Bar Chart Saved!")

############################################################

# PART 3 - Scatter Plot
# Simulating Speed vs Distance Relationship

############################################################

print("Drawing Scatter Plot...")

speed  = [round(random.uniform(0.5, 3.0), 2)
          for _ in range(20)]                # 20 random speeds
distance = [round(s * random.uniform(8, 12), 2)
            for s in speed]                #distance depends on speed

plt.figure(figsize=(6, 4))
plt.scatter(speed, distance, color="purple", marker="x", s=80)
plt.title("Robot Speed Vs Distance Travelled")
plt.xlabel("Speed (m/s)")
plt.ylabel("Distance (m)")
plt.grid(True)
plt.tight_layout()
plt.savefig("day11_scatter_plot.png")
plt.show()
print("Scatter plot saved!")

# ============================================
# PART 4 — Multiple Plots (Subplots)
# Show all 3 charts together in one window
# ============================================

print("Drawing Subplots...")

fig, axes = plt.subplots(1, 3, figsize=(14, 4))    # 1 row, 3 columns

# Subplot 1 — Line chart
axes[0].plot(time_steps, [2.1, 2.4, 2.8, 3.0, 2.7, 2.3, 2.0, 1.8, 1.5, 1.2], color="blue", marker="o")
axes[0].set_title("LIDAR Readings")
axes[0].set_xlabel("Time (s)")
axes[0].set_ylabel("Distance (m)")
axes[0].grid(True)

# Subplot 2 — Bar chart
axes[1].bar(robots, battery, color=colors)
axes[1].set_title("Battery Levels")
axes[1].set_xlabel("Robot")
axes[1].set_ylabel("Battery (%)")
axes[1].set_ylim(0, 100)

# Subplot 3 — Scatter plot
axes[2].scatter(speed, distance, color="purple", marker="x", s=80)
axes[2].set_title("Speed vs Distance")
axes[2].set_xlabel("Speed (m/s)")
axes[2].set_ylabel("Distance (m)")
axes[2].grid(True)

plt.tight_layout()
plt.savefig("day11_subplots.png")
plt.show()
print("Subplots saved!")


