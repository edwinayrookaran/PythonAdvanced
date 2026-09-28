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