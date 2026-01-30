# Day: 35:- 
# Types of Inheritance in Python
# Python supports 5 types of inheritance:
# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance
# Hybrid Inheritance



# Single Inheritance
# Definition
# When a child class inherits from only one parent class.
# Parent → Child

# Example Code
# Output
# Grand Complex
# Father Complex

# Multigible Inheritance
# Definition
# When a child class inherits from more than one parent class.
# Parent1   Parent2
#      \     /
#       Child

# Example Code

# Output
# House
# Jewellery
# Bike




# Multilevel Inheritance
# Definition
# When a class is derived from a class. which is also derived from another class.
# Grandfather → Father → Son → Grandson

# Example Code

# Output
# Grand Complex
# Father Complex
# Son Complex
# Grandson Complex

# 📌 Child can access all ancestor properties.

# Hierarchical Inheritance
# Definition
# When multiple child classes inherit from the same parent class.
#        Father
#        /      \
#    Child1   Child2

# Example Code

# Output
# Bharat Petroleum
# BMW
# Bharat Petroleum
# Fortuner

# 📌 Both children share same parent property.


# Hybrid Inheritance
# Definition
# Hybrid inheritance is a combination of two or more types of inheritance
#  (Single + Multiple + Multilevel).

# Example Structure
# Grandfather
#      |
#    Father
#      |
#     Son
#      |
#   Grandson  (inherits from multiple paths)

# Example Code


# Output
# Grandson Complex

# 📌 Hybrid inheritance = Multilevel + Multiple inheritance