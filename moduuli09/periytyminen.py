"""class Animal:
    def __init__(self,species):
        self.species = species

class Dog(Animal):

    def __init__(self,species,breed):
        super().__init__(species)
        self.breed = breed

animal1 = Animal('Dog')
animal2 = Animal('Cat')
dog1 = Dog("Dog","Husky")
dog2 = Dog("Dog","Mayris")"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def greeting(self):
        print(f"My name is {self.name} and I'm {self.age} years old")

class Student(Person):
    def __init__(self,name, age, id):
        super().__init__(name,age)
        self.id = id

    def greeting(self):
        super().greeting()
        print(f"My id is {self.id}")

person1 = Person("John",22)
student1 = Student("Keijo",22,21313123)
student1.greeting()
person1.greeting()