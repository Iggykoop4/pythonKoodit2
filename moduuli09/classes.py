class Dog:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return f"Tämä kuuluun luokkaan Dog ja koiran nimi on {self.name}"

dog1 = Dog("Rufus")
god2 = Dog("Sirius")
print(dog1)