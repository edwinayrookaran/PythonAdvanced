# 1.Create a class named Movie with attributes moviename,year,language,director,rating
# and methods display_details() and update_rating()

class Movie:
    def __init__(self):
        self.movie_name=input("Enter movie name:")
        self.year=int(input("Enter Year:"))
        self.language=input("Enter language:")
        self.director=input("Enter director:")
        self.rating=float(input("Enter rating:"))

    def display_details(self):
        print("Movie name:",self.movie_name)
        print("Year:",self.year)
        print("Language:",self.language)
        print("Director:",self.director)
        print("Rating:",self.rating)

    def update_rating(self):
        self.rating=float(input("Enter updated rating:"))
        print("Updated Rating:",self.rating)

m=Movie()
m.display_details()
m.update_rating()

# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.

class Vehicle:
    def __init__(self):
        self.brand=input("Enter Brand name:")
        self.model=input("Enter model:")
        self.color=input("Enter color:")
        self.year=int(input("Enter year:"))

    def display(self):
        print("Brand name:",self.brand)
        print("Model:",self.model)
        print("color:",self.color)
        print("Year:",self.year)

class Car(Vehicle):
    def __init__(self):
        print("Car details")
        super().__init__()
        self.mileage=float(input("Enter mileage:"))

    def display(self):
        super().display()
        print("Mileage:",self.mileage)

class Bike(Vehicle):
    def __init__(self):
        print("Bike details")
        super().__init__()
        self.cc=int(input("Enter cc:"))

    def display(self):
        super().display()
        print("cc:",self.cc)

c=Car()
b=Bike()
c.display()
b.display()
