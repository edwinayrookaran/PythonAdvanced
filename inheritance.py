# class Parent:
#     def m1(self):
#         print("in parent class method m1")
#     def m2(self):
#         print("in parent class method m2")
#
# class Child(Parent):
#     def m1(self):       #method overriding
#         super().m1()  #used to completely modify or extend parent functionality
#         print("in child class method m1")
#     def m3(self):
#         print("in child class method m3")
#
# c=Child()
# c.m1()
# c.m2()
# c.m3()

# class Person:
#     def __init__(self):
#         self.name=input("Enter name:")
#         self.age=(int(input("Enter age:")))
#
#     def show(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("Enter roll number:"))
#         self.mark=int(input("Enter mark:"))
#
#     def show(self):
#         super().show()
#         print("Roll number:",self.rollno)
#         print("Mark:",self.mark)
#
# s=Student()
# s.show()

# class Category:
#     def __init__(self):
#         self.category_name=input("Enter category name:")
#
#     def showcategory(self):
#         print("Category name:",self.category_name)
#
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name=input("Enter product name:")
#         self.price=int(input("Enter price:"))
#         self.quantity = int(input("Enter quantity:"))
#
#     def total_price(self):
#         super().showcategory()
#         print("Total Price:",self.price*self.quantity)
#
# p=Product()
# p.total_price()

# class Company:
#     def __init__(self):
#         self.company_name=input("Enter company name:")
#         self.location=input("Enter company location:")
#
#     def display_company(self):
#         print("Company name:",self.company_name)
#         print("Location:",self.location)
#
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.emp_id=int(input("Enter Employee id:"))
#         self.emp_name=input("Enter Employee name:")
#         self.salary=int(input("Enter salary:"))
#
#     def display_details(self):
#         print("Employee id:",self.emp_id)
#         print("name:",self.emp_name)
#         print("Salary:",self.salary)
#         super().display_company()
#
#     def update_salary(self):
#         self.salary=self.salary+self.salary*.1
#         print("New salary:",self.salary)
#
# e=Employee()
# e.display_details()
# e.update_salary()

# multiple inheritance

# class Hospital:
#     def __init__(self):
#         self.hos_name=input("Enter Hospital name:")
#         self.location=input("Enter location:")
#         self.phone=int(input("Enter Phone number:"))
#
#     def display_hospital(self):
#         print("Hospital name:",self.hos_name)
#         print("Location:",self.location)
#         print("Phone number:",self.phone)
#
# class Department:
#     def __init__(self):
#         self.dept_name=input("Enter department name:")
#         self.doc_name=input("Enter doctor name:")
#
#     def display_department(self):
#         print("Department name:",self.dept_name)
#         print("Doctor name:",self.doc_name)
#
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.pat_name=input("Enter patient name:")
#         self.age=int(input("Enter age:"))
#         self.gender=input("Enter gender:")
#         self.phone=int(input("Enter phone number:"))
#         self.adm_date=input("Enter Admission date:")
#         self.bed_no=int(input("Enter Bed number:"))
#         self.dis_date=""
#     def set_discharge(self):
#         self.dis_date = input("Enter updated discharge date:")
#
#     def full_summary(self):
#         Hospital.display_hospital(self)
#         Department.display_department(self)
#         print("patient name:",self.pat_name)
#         print("age:",self.age)
#         print("gender:",self.gender)
#         print("Phone number:",self.phone)
#         print("Admission_date",self.adm_date)
#         print("Bed number:",self.bed_no)
#         if (self.dis_date==""):
#             print("Not yet discharged")
#         else:
#             print("Discharge date:",self.dis_date)
#
# p=Patient()
# p.full_summary()
# p.set_discharge()
# p.full_summary()


# class A:
#     def f(self):
#         print("first function")
#     def f(self,a):
#         print("second function")
#     def f(self,a,b):
#         print("third function")
#
# a=A()
# # a.f()
# # a.f(10)
# a.f(10,20)