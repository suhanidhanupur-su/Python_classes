# Day: 26
# Set Methods + Typecasting + Dictionary Introduction
# pop() – remove random element from a set
# ex:

# Output
# before pop: {33, 'rahul', 8.8, 11, 22, 'ravi'}
# after pop: {'rahul', 8.8, 11, 22, 'ravi'}

# Note: It removes a random element because sets are unordered.

# discard() – remove specific element (NO error if not found)
# ex:

# Output
# before discard: {'rahul', 33, 8.8, 11, 22, 'ravi'}
# after discard: {'rahul', 33, 8.8, 11, 22, 'ravi'}


# Since the element doesn’t exist → No error

# clear() – remove all elements from set
# ex:

# Output
# before clear: {'rahul', 33, 8.8, 11, 22, 'ravi'}
# after clear: set()

# 📌 TYPECASTING
# Typecasting = Converting one data type into another
# Types of Typecasting in Python
# 1️⃣ Explicit Typecasting
# 2️⃣ Implicit Typecasting


# 1️⃣ Explicit Typecasting
# (Developer converts manually)
# String → Integer
# Example:
# Output
# <class 'str'>
# 23
# <class 'int'>



# Integer → String
# example:
# Output
# <class 'int'>
# 23
# <class 'str'>



# Boolean → Integer
# example:

# Output
# <class 'bool'>
# 1
# <class 'int'>



# Integer → Boolean
# example:

# Output
# <class 'int'>
# True
# <class 'bool'>


# ✔ Rule:
# bool(non-zero number) → True  
# bool(0) → False

# example:
# Output
# <class 'int'>
# False
# <class 'bool'>



# # 2️⃣ Implicit Typecasting
# # (Python automatically converts)
# Example:
# Output
# <class 'float'>
# <class 'int'>
# after implicit typecasting: 10.7


# ➡ int + float → float automatically

# 🧾 DICTIONARY INTRODUCTION
# A dictionary stores data in key-value pairs
#  ✔ mutable
#  ✔ ordered
#  ✔ keys must be unique and immutable
# Example



# Output
# {'name': 'Ujwal', 'age': 24, 'city': 'Bangalore', 'roll_no': 101}



# Key = Left side
# Value = Right side
# Example:



# 📌 Difference:
#  List stores only values
#  Dictionary stores key + value together



