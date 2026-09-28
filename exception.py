# try:
#     n1=int(input("Enter number:"))
#     n2=int(input("Enter number:"))
#     r=n1/n2
# except ValueError as e:
#     print(e)
#     print(type(e))
# except ZeroDivisionError:
#     print("Zero Division Error")
# except:
#     print("Error")
# else:
#     print("Result:",r)
# finally:
#     print("Done")
#
# # write a program that takes a number as input from user and finds the factorial of that number
# # using math.factorial().use a try -except block to handle the value error if user inputs a
# # number/character input

# import math
# def fact():
#     try:
#         n=int(input("Enter a number:"))
#         f=math.factorial(n)
#         print("Factorial:",f)
#     except ValueError:
#         print("Value Error")
#         fact()   # recursive function-a function that calls itself
# fact()

# # Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# # and division based on user choice. Handle invalid inputs and division by zero using exception handling.
#
# try:
#     n1=int(input("Enter n1:"))
#     n2=int(input("Enter n2:"))
#     op=input("Enter operator:")
#     if op=="+":
#         print("Sum:",n1+n2)
#     elif op=="-":
#         print("Difference:",n1-n2)
#     elif op=="*":
#         print("Product:",n1*n2)
#     elif op=="/":
#         print("Quotient:",n1/n2)
#     else:
#         print("Invalid operator")
# except ZeroDivisionError:
#     print("Zero Division Error")
# except:
#     print("Invalid input")
#
# # write a program to open a file (text file) in read mode
# # if the file does not exist catch the file exception print the error message file does not
# # exist
# try:
#     filename=input("Enter filename:")
#     f=open(filename,"r")
#     print("File opened successfully")
#     f.close()
# except:
#     print("File does not exist")
#
# #Given a Dictionary
# # Write a program to ask the user to enter a key and display its value.
# # Handle KeyError if key does not exist
# d={"name":"arun","age":23,"place":"ekm"}
# try:
#     k=input("Enter key:")
#     print(d[k])
# except KeyError:
#     print("key does not exist")

# class MyException(Exception):
#     pass
# try:
#     n=int(input("Enter age:"))
#     if(n<18):
#         raise MyException("Not eligible for voting")
#     else:
#         print("eligible for voting")
# except MyException as e:
#     print(e)

#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
# try:
#     n=int(input("Enter a number:"))
#     if(n<=0):
#         raise ValueError("Number must be positive")
# except ValueError as e:
#     print(e)
#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")
# class CustomerException(Exception):
#     pass
# try:
#     n=input("Enter Password:")
#     if len(n)<8:
#         raise CustomerException("Password should be 8 characters")
# except CustomerException as e:
#     print(e)

#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

# class InsuffientBalanceError(Exception):
#     pass
#
# try:
#     amount=int(input("Enter amount:"))
#     balance=int(input("Enter balance"))
#     if amount>balance:
#         raise InsuffientBalanceError("Not Enough Balance.Transaction Failed")
# except InsuffientBalanceError as e:
#     print(e)