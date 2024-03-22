#class Ostoslista:
    #def __init__(self,lista):
        #self.lista = lista

    #def __repr__(self):
        #return f" Ostoslista: {self.lista}"

class School:
    def __init__(self,name):
        self.name = name



class Book:
    def __init__(self,name,title):
        self.name = name
        self.title = title

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def addbook(self,book):
        self.books.append(book)

class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.courses = []

    def addcourse(self,course):
        self.courses.append(course)

class Course:
    def __init__(self,name)
        self.name = name
        self.students = []

    def addstudent(self,name):
        self.students.append(Student)

library1 = Library("Kallion kirjasto")
library2 = Library("Karakallion kirjasto")
book1 = Book("Harry Potter","Fiery wand")
book2 = Book("Prison Break","Sturdy crowbar")
school1 = School("Metropolia")
school2 = School("Laurea")
student1 = Student("Mike",school1)
student2 = Student("John",school2)
library1.addbook(book1)
library1.addbook(book2)
library2.addbook(book1)
#lista1 = Ostoslista(["Milk","Cheese","Bread","Butter"])
#print(lista1.lista)
print(school1.name)
print(school2.name)
print(f"{student1.name} studies at {student1.school.name}")
print(f"{student2.name} studies at {student2.school.name}")
for i in library1.books:
    print(f"{i.name} {i.title} at {library1.name}")

student1 = Student("Mike")
student2 = Student("John")
student3 = Student("Ike")

course1 = Course("Math")
course2 = Course("Physics")
course3 = Course("Arts")



