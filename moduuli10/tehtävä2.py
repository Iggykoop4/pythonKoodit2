"""Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building. Write a method called run_elevator that accepts
the number of the elevator and the destination floor as its parameters. In the main program, write the statements for creating a new building and running the elevators of the building.
"""

"""Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
 The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
 If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor."""

class Elevator():
    def __init__(self,bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self,floor_chosen):
        if floor_chosen < self.bottom_floor or floor_chosen > self.top_floor:
            print(f"floor {floor_chosen} is out of reach")
            return
        while self.current_floor != floor_chosen:
            if self.current_floor < floor_chosen:
                self.floor_up()
            else:
                self.current_floor > floor_chosen
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}.")
        else:
            print("Elevator is already at the top floor.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}.")
        else:
            print("Elevator is already at the bottom floor.")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 1 or elevator_number > len(self.elevators):
            print(f"Elevator number {elevator_number} does not exist.")
            return
        self.elevators[elevator_number - 1].go_to_floor(destination_floor)

    def print_elevator_floors(self):
        for i, elevator in enumerate(self.elevators, start=1):
            print(f"Elevator number {i} is at floor {elevator.current_floor}")


if __name__ == "__main__":
    building = Building(1, 10, 3)
    building.run_elevator(1, 8)
    building.run_elevator(2, 5)
    building.run_elevator(3, 10)
    building.print_elevator_floors()
