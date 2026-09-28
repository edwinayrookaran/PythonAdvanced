# from abc import ABC,abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self):
#         print("Rectangle")
#         self.l = int(input("Enter length:"))
#         self.b=int(input("Enter Breadth:"))
#     def get_area(self):
#         area=self.l*self.b
#         print("Area=",area)
#     def get_perimeter(self):
#         p=2*(self.l+self.b)
#         print("Perimeter=",p)
#
# class Square(Shape):
#     def __init__(self):
#         print("Square")
#         self.a=int(input("Enter the side length:"))
#
#     def get_area(self):
#         area=self.a*self.a
#         print("area=",area)
#
#     def get_perimeter(self):
#         p=4*self.a
#         print("perimeter=",p)
#
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
# s=Square()
# s.get_area()
# s.get_perimeter()

# from abc import ABC,abstractmethod
# class Employee(ABC):
#     def __init__(self):
#         self.emp_id=int(input("Enter Employee id:"))
#         self.name=input("Enter name:")
#         self.age=int(input("Enter age:"))
#
#     @abstractmethod
#     def calculate_salary(self):
#         pass
#
# class Fulltime(Employee):
#     def __init__(self):
#         print("Full time employee")
#         super().__init__()
#         self.mon_salary=int(input("Enter monthly salary:"))
#
#     def calculate_salary(self):
#         print("Salary:",self.mon_salary)
#
# class Parttime(Employee):
#     def __init__(self):
#         print("Part time employee")
#         super().__init__()
#         self.hour=int(input("Enter Hours:"))
#         self.rate=int(input("Enter rate:"))
#
#     def calculate_salary(self):
#         print("salary=",self.hour*self.rate)
#
# f=Fulltime()
# f.calculate_salary()
# p=Parttime()
# p.calculate_salary()



