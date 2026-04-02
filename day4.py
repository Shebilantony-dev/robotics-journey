#For Loop - Counting
print("\n--- Robot Steps ---")
for step in range(5):
    print(f"\nRobot taking step {step + 1}")


#For Loop - List
print("\n--- Robot Sensors ---")
sensors = ["Camera", "GPS", "Ultrasonic", "Infrared"]
for sensor in sensors:
    print(f"Checking Sensor: {sensor}")


#While Loop
print("\n--- Battery Monitor ---")
battery = 100
while battery > 50:
    print(f"Battery Level : {battery}% - Robot is Active! ")
    battery -= 20
print(f"Battery Level : {battery}% - Battery Low! Charging! ")


#Loop With if/else Inside
print("\n--- Obstacle Detection ---")
distances = [100, 45, 80, 20, 60]
for distance in distances:
    if distance < 50:
        print(f"distance = {distance}cm - Obstacle Detected! Stop!")
    else:
        print(f"distance = {distance}cm - Path clear! Move Forward! ")
        
