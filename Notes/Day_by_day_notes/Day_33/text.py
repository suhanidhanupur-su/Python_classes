# Day:33:- 
# OOPs Programming – Revision
# OOPs = Object Oriented Programming System
# Python supports OOPs, which helps in writing:
# Clean code

# Reusable code

# Organized structure

# Variable With Function (Normal Way)
# code:

# Class Variable (Wrong Way)
class Student:
    std_name = "Aditya"

print(std_name)   # ERROR

# 📌 Reason:
#  Class variables cannot be accessed directly without object or class name.

# Class Variable (Correct Way Using Object)
# code:
# Output
# Aditya


# Real-Life Example (Understanding Object)
# Principal   → Class
# Vice Principal → Object

# Object works on behalf of class.

# Class Method Without Object (Wrong)
class Student:
    def student_info(self):
        print("here is all about student info")

student_info()   # ERROR

# 📌 Reason:
#  Methods must be called using object.



# Class Method With Object (Correct)
# code:

# Output
# here is all about student info


# Another Class Example
# code:
# Output
# Veenu Restaurant
# Gupta Sweets


# Private Variables in Class
# code:

# 📌 Reason:
#  Variables starting with __ are private
#  They cannot be accessed directly outside the class.

# What is a Class? (Theory)
# A class is a blueprint/template


# It defines:


# Variables (properties)
# Methods (functions)



# What is an Object?
# An object is an instance of a class
# It represents a real-world entity
# It contains:


# Variables
# Methods



# Another Class Example


# Final Example Class


# Output
# Gupta Sweets
# aditya assets


# ❌ Wrong Way
# print(hotel)   # ERROR

# 📌 Reason:
#  Class variables must be accessed via object or class name.
# OOPs – 4 Pillars ( Home Work )
# 1️⃣ Inheritance
# 2️⃣ Encapsulation
# 3️⃣ Polymorphism
# 4️⃣ Abstraction

