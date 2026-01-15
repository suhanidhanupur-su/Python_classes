# Day: 32:- 
# OOPs Programming
# OOPs stands for Object Oriented Programming System.
# Languages Support OOPs
# ❌ C (does not support OOPs)


# ✅ C++


# ✅ Java


# ✅ Python


# ✅ JavaScript


# ✅ PHP



# Flow of Programming
# Variable  →  Function  →  Class


# Global Variable & Local Variable (Revision)
# Local Variable
# Declared inside a function


# Can be accessed only inside that function



# Global Variable
# Declared outside a function


# Can be accessed anywhere in the program



# Example: Local Variable

# Output
# here is the student information
# inside this function: Shivam


# ❌ Error Example (Accessing Local Variable Outside)
# def student_info():
#     std_name = "Shivam"

# student_info()
# print(std_name)   # ERROR



# 📌 Reason:
#  std_name is a local variable, not accessible outside the function.


# Global Variable Example



# Output
# inside function global: Ujwal
# inside function local: Shivam
# outside function: Ujwal

# 📘 Class in Python
# A class is a blueprint of an object.
#  It contains:
# Variables (data)
# Functions (methods)

# Example: Class Without Object (Wrong Way)
# class Student:
#     std_name = "Aditya"
#     std_roll = "111"

# print(std_name)   # ERROR



# 📌 Reason:
#  Class variables must be accessed using object or class name.
# Correct Way: Using Object

# Output
# Aditya
# 111


# Class with Method
# class Student:
#     def student_info(self):
#         print("here is all about student info")


# ❌ Wrong Way (Without Object)
# student_info()   # ERROR


# ✅ Correct Way (Using Object)

# Output
# here is all about student info

