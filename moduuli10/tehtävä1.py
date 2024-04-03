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


if __name__ == "__main__":
    elevator = Elevator(1, 10)
    elevator.go_to_floor(8)
    elevator.go_to_floor(1)
