# Day: 34:- 
# What is Inheritance?
# Inheritance means:
# Child class inherits properties and methods of Parent class
# 📌 Real-life meaning:
#  Bachcha apne parents ke features / property inherit karta hai.

# Why Inheritance is Used?
# Code reusability


# Avoid duplication


# Easy maintenance


# Clear relationship between classes



# Before Inheritance (Problem Case)
# code:-




# ❌ Output : AttributeError

# 📌 Reason:
#  Son class does not inherit Father class.

# Single Inheritance (Correct Way)
# code:-


# ✅ Output
# Mohit Pan Dukan
# Bhardwaj Empire

# 📌 Son(Father) → Son inherits Father




# Understanding Inheritance (Real-Life Example)
# Sourabh (Father)
# │
# └── Rohit (Son)
#      └── Property: Bhardwaj Villa

# 📌 Rohit gets property because Sourabh is his father.

# Another Simple Example
# code:-


# Output
# TCS
# It's all about this company



# Class Without Object (Wrong)
# class Virat_Kohli:
#     jersey_no = 18
#     bat_brand = "MRF"

# print(jersey_no)   # ERROR


# 📌 Class variables must be accessed using object or class name

# Class With Object (Correct)
# code:-
# Output
# 18




