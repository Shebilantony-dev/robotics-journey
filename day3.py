# Condition & if/else
# Robotics Journey



# Simple if/else
battery_level = 85

if battery_level > 50:
    print("Robot Battery is Good! Let's Go!")
else:
    print("Robot Battery is Low! Please Recharge!")




# elif Multiple conditions
speed = 10 
if speed < 5:
    print("Robot is moving Slowly!")
elif speed < 15:
    print("Robot is moving at Normal speed!")
else:
    print("Robot is moving fast")



# Combinig Conditions
is_robot_active = True
obstacle_detected = False

if is_robot_active and not obstacle_detected:
    print("Robot is moving Forward!")
elif is_robot_active and obstacle_detected:
    print("Robot stopped! Obstacle detected!")
else:
    print("Robot is inactive!")
