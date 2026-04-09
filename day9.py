# =======================================================
# Day 9: Classes & Object-oriented programming
# Basic of ROS2
# =======================================================


#--- 1. Define a Class ---
class Robot:
    """A simple Robot class - like a ROS2 Node blueprint!"""

    #--- 2. Constructor (__init__) ---
    def __init__(self, name, model, battery):
        self.name    = name        #Attribute
        self.model   = model       #Attribute
        self.battery = battery     #Attribute
        print(f"[INIT] Robot '{self.name}' is ready!")

    #--- 3. Methods ---
    def move(self,direction):
        print(f"[MOVE] {self.name} is moving {direction}.")

    def check_battery(self):
        if self.battery > 20:
            print(f"[BATTERY] {self.name}: BAttery OK - {self.battery}%")
        else:
            print(f"[BATTERY] {self.name}: Low BAttery! {self.battery}%")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"[CHARGE] {self.name} Charged! Battery now at {self.battery}%")

    def status(self):
        print(f"\n--- {self.name} Status ---")
        print(f"  Model  : {self.model}")
        print(f"  Battery: {self.battery}")


#--- 4. Inheritance (Like ROS@ Node!) ----
class SensorRobot(Robot):
    """Extends Robot with a sensor - Just like ROS2 Subscriber Nodes!"""

    def __init__(self, name, model, battery, sensor_type):
        super().__init__(name, model, battery)             #Call parent __init__
        self.sensor_type = sensor_type
        print(f"[SENSOR] Sensor '{self.sensor_type}' attached to {self.name}")

    def read_sensor(self):
        import random
        value = round(random.uniform(0.5, 5.0), 2)
        print(f"[SENSOR] {self.name} reads {self.sensor_type}: {value} m")


#=============================================================
# Main Program
#=============================================================

print("=" * 45)
print("  Day 9: Classes & OOP - Robotic Journey")
print("=" * 45)


# Create Objects (instances)
robot1 = Robot("Alpha", "RX-100", 80)
robot2 = Robot("Beta", "RX-200", 15)

print()

# Use Methods
robot1.move("forward")
robot1.check_battery()

robot2.check_battery()
robot2.charge(50)

print()

# Inheritance in Action!
sensor_bot = SensorRobot("Gamma", "SX-300", 90, "LIDAR")
sensor_bot.move("left")
sensor_bot.read_sensor()
sensor_bot.read_sensor()

print()

# Status Report
robot1.status()
sensor_bot.status()

print("\n [Done] Day 9 Complete! OOP Unlocked!")
