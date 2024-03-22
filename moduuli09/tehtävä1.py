class Car:
    def __init__(self,reg_number,max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0



car = Car("ABC-123", 142)
print(f" new car = reg.number: {car.reg_number}, max speed: {car.max_speed}, current speed: {car.current_speed}, distance traveled: {car.distance_traveled}")

