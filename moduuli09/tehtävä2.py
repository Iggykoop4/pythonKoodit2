class Car:
    def __init__(self,reg_number,max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0


    def accelerate(self,speed_change):
        if speed_chan > 0:
            self.current_speed = min(self.current_speed + speed_change, self.max_speed)
        elif speed_change < 0:
            self.current_speed = max(self.current_spee + speed_change,0)

car = Car("ABC-123", 142)
print(f" new car = reg.number: {car.reg_number}, max speed: {car.max_speed}, current speed: {car.current_speed}, distance traveled: {car.distance_traveled}")

