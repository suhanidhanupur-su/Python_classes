# Day: 21

# 1. Mutable and Immutable
# Mutable OR Changeable: => it can be changed entirely as well as specifically.
# Example: List, Dictionary, Set

# Immutable OR Unchangeable: => it can be changed entirely but not specifically.
# Example: Tuple, String, Frozen Set


# -> Mutable and Immutable Example Explain
# Mutable example: List

#code
# Output
# before changes : [11, 22, 33, 44, 55]
# after changes  : [11, 22, 777, 44, 55]


# listt is a mutable object.
# The element at index 2 is changed from 33 to 777 without creating a new list.

# Immutable example: String

#  0 1 2 3 4 5
#  A d i t y a




# Output
# before changes : Wilmot
# After Changes W


# Strings are immutable, so this kind of change is not allowed:
# python
# my_name[0] = "Z"  # Error: Strings are immutable
# print("after changes  :", my_name)


# But reassigning the whole variable is allowed (new string object is created):
# python
# code
# Output
# before changes : Suhani
# after changes  : Nisha


# Tuple: basic concept
# A tuple is a collection which is immutable and ordered.
# It cannot be changed after creation.
# python
# code

# Output
# (122, 222, 322, 42, 52)
# Tuple length


# len(my_tuple) gives the number of elements in the tuple.

# Types of brackets
# ( ) => Parenthesis
# [ ] => Square brackets
# { } => Curly braces

# Tuple indexing
# python
# code

# Output:

# (122, 222, 322, 42, 52)
# 122
# 52


# Index 0 gives the first element.
# Index 4 gives the last element.



# The for loop prints each element of the tuple one by one.

# Tuple methods
# count() – returns the number of occurrences of any element
# python



# index() – returns the index of first occurrence

# code


# len() – returns number of elements
# code



# Negative indexing in tuple
# python
# #           -5   -4   -3   -2  -1

# -1 refers to the last element (52).
# -2 refers to the second last element (42).

