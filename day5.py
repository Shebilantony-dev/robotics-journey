#Day 5 - Functions


#Basic Function
def greet_robot():
    print("Hello! I am a Robot!")


#Function with Paramiters
def check_battery(battery_level):
    if battery_level > 50:
        print(f"Battery is Good: {battery_level}% Let's Go!")
    else:
        print(f"BAttery is Low: {battery_level}% Charge Me!")


# Function with Return Value
def calculate_speed(distance, time):
    speed = distance / time
    return speed


# Function Combining Everything
def robot_status(name, battery, distance, time):
    print(f"\n--- Robot Status Report ---")
    print(f"Robot Name: {name}")
    check_battery(battery)
    speed = calculate_speed(distance, time)
    print(f"Current Speed: {speed} m/s ")
    if speed > 5:
        print(f"Moving Fast!")
    else:
        print(f"Moving Slow!")


# Call Functions
greet_robot()
check_battery(80)
check_battery(30)
robot_status("Jarvis", 75, 100, 20)
robot_status("Jarvis", 40, 50, 20)
