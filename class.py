#example 1
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog(name="Buddy", age=3)
my_dog = Dog(name="sheero", age=4 )

print(f"{my_dog.name} is {my_dog.age} years old.")
my_dog.bark()

#example 2
class Occupation:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} does {self.occupation} for a living.")
a = Occupation("shruti", "student")
b = Occupation("shinchan","comedian")

a.info()
b.info()

#example 3
class Student:
    def __init__(self, name, rollno, percentage, grade):
        self.name = name
        self.rollno = rollno
        self.percentage = percentage
        self.grade = grade
    def info(self):
        print(f"{self.name} ,who's rollno is {self.rollno} has scored {self.percentage} in exam and the grade is {self.grade}"
               )
a = Student("Navi","23","93%","A")
a.info()

#example 4
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")

lion = Animal("lion", "roar")
dog = Animal("dog", "bark")

lion.make_sound()
dog.make_sound()

#example 5
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
# Creating instances of the Rectangle class
rectangle1 = Rectangle(5, 8)
rectangle2 = Rectangle(10, 3)

# Calculating and printing the area for each rectangle
print(f"Area of Rectangle 1: {rectangle1.calculate_area()}")
print(f"Area of Rectangle 2: {rectangle2.calculate_area()}")
