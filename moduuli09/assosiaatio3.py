class Dog:
    def __init__(self, name, birth_year, sound="Woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.name + " barks: " + self.sound)
        return
dog1 = Dog("John", 1999)
print(dog1.name, dog1.birth_year)
dog1.bark(4)