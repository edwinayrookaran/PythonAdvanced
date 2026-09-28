# class Person:
#     def __init__(self,n,a):  #constructor method
#                              #used to initialize object properties
#         self.name=n
#         self.age=a
#
#     def show(self):     #self keyword used to refer current  object
#         print(self.name,self.age)
#
# p1=Person(n,a)    #creates object p1
#                               #calls __init__ function defined inside class Person
# p1.show()

# class Person:
#     def __init__(self):  #constructor method
#                              #used to initialize object properties
#         self.name=input("Enter name:")
#         self.age=int(input("Enter age:"))
#
#     def show(self):     #self keyword used to refer current  object
#         print(self.name,self.age)
#
# p1=Person()    #creates object p1
#                 #calls __init__ function defined inside class Person
# p1.show()

#define a class named employee with attributes empid,name,age,salary,designation
# and methods getsalary() and showpersonaldetails()

# class employee:
#     def __init__(self):
#         self.empid=int(input("Enter employee id:"))
#         self.name=input("Enter name:")
#         self.age = int(input("Enter age:"))
#         self.salary=int(input("Enter salary:"))
#         self.desgn=input("Enter designation:")
#
#     def getsalary(self):
#             print("salary:",self.salary)
#
#     def showpersonaldetails(self):
#             print("Name:",self.name)
#             print("Age:",self.age)
#
# e1=employee()
# e1.getsalary()
# e1.showpersonaldetails()

# define a class named student with attributes rollno,name,mark1,mark2,mark3
# methods display() to display rollno and total mark of a student

# class Student:
#     def __init__(self):
#         self.rollno = int(input("Enter roll number:"))
#         self.name=input("Enter name:")
#         self.mark1 = int(input("Enter mark1:"))
#         self.mark2 = int(input("Enter mark2:"))
#         self.mark3 = int(input("Enter mark3:"))
#
#     def display(self):
#         print("roll number:",self.rollno,"Total marks:",self.mark1+self.mark2+self.mark3)
#
# s1=Student()
# s1.display()

# class Book:
#     def __init__(self):
#         self.title = input("Enter title name:")
#         self.author=input("Enter author name:")
#         self.price = int(input("Enter price:"))
#         self.pages = int(input("Enter pages:"))
#         self.language = input("Enter language:")
#
#     def gettitle(self):
#         print("Title:",self.title)
#
#     def settitle(self):
#         self.title=input("Enter new title name:")
#         self.gettitle()
#
# b1=Book()
# b1.gettitle()
# b1.settitle()

# class Account:
#     def __init__(self):
#         self.accname = input("Enter account name:")
#         self.accno=int(input("Enter account number:"))
#         self.balance = int(input("Enter balance:"))
#
#     def withdraw(self):
#         amount=int(input("Enter amount to withdraw:"))
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance=self.balance-amount
#             self.showbalance()
#
#     def deposit(self):
#         amount = int(input("Enter amount to deposit:"))
#         self.balance = self.balance + amount
#         self.showbalance()
#
#     def showbalance(self):
#         print("Balance:",self.balance)
#
# a1=Account()
# a2=Account()
# a.withdraw()
# a.deposit()

# l=[10,20,30]

# l=['red','green','blue']
# l=[a1,a2]
# for i in l:
#     print(i.accname)
#     i.showbalance()

# class Account:
#     def __init__(self):
#         self.accno = int(input("Enter account number:"))
#         self.accname = input("Enter account name:")
#         self.balance = int(input("Enter balance:"))
#
#     def withdraw(self):
#         amount=int(input("Enter amount to withdraw:"))
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance=self.balance-amount
#             self.showbalance()
#
#     def deposit(self):
#         amount = int(input("Enter amount to deposit:"))
#         self.balance = self.balance + amount
#         self.showbalance()
#
#     def showbalance(self):
#         print("Balance:",self.balance)
#
# l=[]
# while(1):
#     print("1.create an account")
#     print("2.withdraw")
#     print("3.deposit")
#     print("4.show balance")
#     print("5.exit")
#
#     ch=int(input("Enter your choice:"))
#
#     if ch==1:
#         a=Account()
#         l.append(a)
#         print(l)
#     elif ch==2:
#         n=int(input("Enter Account number:"))
#         for i in l:
#             if(i.accno==n):
#                 i.withdraw()
#                 break
#         else:
#             print("No account Found")
#     elif ch==3:
#         n = int(input("Enter Account number:"))
#         for i in l:
#             if (i.accno == n):
#                 i.deposit()
#                 break
#         else:
#             print("No account Found")
#     elif ch==4:
#         n = int(input("Enter Account number:"))
#         for i in l:
#             if (i.accno == n):
#                 i.showbalance()
#                 break
#         else:
#             print("No account Found")
#     else:
#         exit()


#Write a menu-driven Python program using a class Student to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

class Student:
    def __init__(self):
        self.rollno = int(input("Enter roll number:"))
        self.name = input("Enter student name:")
        self.marks = int(input("Enter marks:"))

    def update(self):
        self.marks=int(input("Enter marks to update"))

    def display(self):
        print("Roll number:",self.rollno)
        print("Student name:",self.name)
        print("marks:",self.marks)



l=[]
while(1):
    print("1.Add Student")
    print("2.update marks")
    print("3.Display student details")
    print("4.search student")
    print("5.delete Student")
    print("6.exit")

    ch=int(input("Enter your choice:"))

    if ch==1:
        s=Student()
        l.append(s)
        print(l)
    elif ch==2:
        n=int(input("Enter Rollno number:"))
        for i in l:
            if(i.rollno==n):
                i.update()
                break
        else:
            print("No student Found")
    elif ch==3:
        for i in l:
            i.display()
    elif ch==4:
        n = int(input("Enter roll number:"))
        for i in l:
            if (i.rollno == n):
                i.display()
                break
        else:
            print("No Student Found")
    elif ch==5:
        n = int(input("Enter roll number:"))
        for i in l:
            if (i.rollno == n):
                l.remove(i)
                break
        else:
            print("No student found")
    else:
        exit()