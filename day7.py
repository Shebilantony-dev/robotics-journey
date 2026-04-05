# Day - 7 File Handling

# Writing to a File
print(f"--- Writing Robot Log ---")
with open("robot_log.txt", "w") as file:
    file.write("Robot Activity Log\n")
    file.write("==================\n")
    file.write("Status: Active\n")
    file.write("Battery: 85%\n")
    file.write("Location: Deggendorf Lab\n")
print("Log File Created!")


# Appending to File
with open("robot_log.txt", "a") as file:
    file.write("Speed = 10.5 m/s \n")
    file.write("Obstacle Detected: No \n")
print("Log File Updated!")


# Reading from a File
print("\n --- Reading Robot Log ---")
with open("robot_log.txt", "r") as file:
    content = file.read()
    print(content)


# Writing Sensor Data Using Loops
print("--- Saving Sensor Data ---")
sensor_data = [
    {"sensor": "Camera", "status": "Active", "value": "1080p"},
    {"sensor": "GPS", "status": "Active", "value": "48.8 degree North"},
    {"sensor": "Ultrasonic", "status": "Active", "value": "45cm"},
    {"sensor": "Battery", "status": "Warning", "value": "35%"},
]

with open("sensor_data.txt", "w") as file:
    for data in sensor_data:
        file.write(f"sensor: {data['sensor']} | Status: {data['status']} | Value: {data['value']}\n")
print("Sensor Data Saved!")


# Reading Sensor Data
print("\n --- Reading Sensor Data ---")
with open("sensor_data.txt", "r") as file:
    for line in file:
        print(line.strip())
