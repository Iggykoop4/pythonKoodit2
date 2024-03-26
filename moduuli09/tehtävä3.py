class Car:
    def __init__(self,reg_number,max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0


    def accelerate(self,speed_change):
        if speed_change > 0:
            self.current_speed = min(self.current_speed + speed_change, self.max_speed)
        elif speed_change < 0:
            self.current_speed = max(self.current_speed + speed_change,0)

    def drive(self,hours):
        distance_traveled = self.current_speed * hours
        self.distance_traveled += distance_traveled

car = Car("ABC-123", 142)

print(f" new car = reg.number: {car.reg_number}, max speed: {car.max_speed}, current speed: {car.current_speed}, distance traveled: {car.distance_traveled}")

car.accelerate(30)
print(f"accelerating to {car.current_speed}")

car.accelerate(70)
print(f"accelerating to {car.current_speed}")

car.accelerate(50)
print(f"accelerating to {car.current_speed}")

car.accelerate(-200)
print(f"using emergency brake! current speed: {car.current_speed}")

"""car.distance_traveled += 200
print(car.distance_traveled)
car.distance_traveled += 500
print(car.distance_traveled)
car.distance_traveled += 1300
print(car.distance_traveled)
car.accelerate(60)
car.drive(1.5)
print(car.distance_traveled)"""

