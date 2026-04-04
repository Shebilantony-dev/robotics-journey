# DAY 6 - Lists & Dictionaries

# Lists
print(f"--- Robot Parts List ---")
robot_parts = ["Camera", "Motor", "Sensor", "Battery", "Arm"]
print(f"All Parts: {robot_parts}")
print(f"First Part: {robot_parts[0]}")
print(f"Last Part: {robot_parts[-1]}")
print(f"Total Parts: {len(robot_parts)}")


# Adding & Removig from Lists
robot_parts.append("Wheels")
print(f"After adding wheels: {robot_parts}")
robot_parts.remove("Motor")
print(f"After removing Motor: {robot_parts}")


# Dictionaries
print(f"\n--- Robot Information ---")
robot = {
    "name": "Atlas",
    "battery": 85,
    "speed": 10.5,
    "is active": True,
    "location": "Deggendorf Lab"
}


print(f"Robot Name: {robot['name']}")
print(f"Battery: {robot['battery']}% ")
print(f"Speed: {robot['speed']} m/s")
print(f"Location: {robot['location']}")


# Update dictionary
robot["battery"] = 60
robot["location"] = "Munich Lab"
print(f"\nUpdated battery: {robot['battery']}%")
print(f"Updated location: {robot['location']}")


# Loop through dictionary
print("\n--- Full Robot Report ---")
for key, value in robot.items():
    print(f"{key}: {value}")