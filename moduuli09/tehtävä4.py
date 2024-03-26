import random
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

def main():
    car_list = []

    for i in range(1,11):
        reg_number = f"ABC-{i}"
        max_speed = random.randint(101,200)
        car = Car(reg_number,max_speed)
        car_list.append(car)

    """for car in car_list:
        print(f"{car.reg_number} MAX speed:{car.max_speed}")"""

    while True:
        for car in car_list:
            speedup = random.randint(-10,15)
            car.accelerate(speedup)
            car.drive(1)
            print(f" {car.reg_number}  {car.max_speed} km/h  {car.current_speed} km/h  {car.distance_traveled} km ")


            if car.distance_traveled >= 10000:
                print(f"Race ended, car {car.reg_number} has won the race!")
                return
        print(f"\nnext round\n")



main()





