class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def addcourse(self, course):
        self.courses.append(course)


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def addstudent(self,student):
        self.students.append(student)

student1 = Student("Mike")
student2 = Student("John")
student3 = Student("Ike")

course1 = Course("Math")
course2 = Course("Physics")
course3 = Course("Arts")

student1.addcourse(course1)
student1.addcourse(course2)
student2.addcourse(course3)
student2.addcourse(course2)
student3.addcourse(course1)
student3.addcourse(course2)
student3.addcourse(course3)
course1.addstudent(student1)
course2.addstudent(student1)
course2.addstudent(student2)
course3.addstudent(student2)
course1.addstudent(student3)
course2.addstudent(student3)
course3.addstudent(student3)


for i in student1.courses:
    print(f"{student1.name} has {i.name}")

for i in student2.courses:
    print(f"{student2.name} has {i.name}")

for i in student3.courses:
    print(f"{student3.name} has {i.name}")

for i in course1.students:
    print(f"{course1.name} course has {i.name}")

for i in course2.students:
    print(f"{course2.name} course has {i.name}")

for i in course3.students:
    print(f"{course3.name} course has {i.name}")






