#        0   1   2   3   4
listt = [11, 22, 33, 44, 55]
print("before changes :", listt)

listt[2] = 777
print("after changes  :", listt)
# -----------------------------------------------
my_name = "Aditya"
print("before changes :", my_name)

print(my_name[0])  # A
# -----------------------------------------------
my_name = "Wilmot"
print("before changes :", my_name)
my_name = "Wilmot"
print("After Changes", my_name[0])  # W
# -----------------------------------------------
name = "Suhani"
print("before changes :", name)

name = "Nisha"   # Entire value reassigned (allowed)
print("after changes  :", name)
# -----------------------------------------------
my_tuple = (122, 222, 322, 42, 52)
print(my_tuple)
# -----------------------------------------------
# Tuple length

my_tuple = (111, 111, 111, 22, 7879)
print(len(my_tuple))   ##
# -----------------------------------------------
#          0     1    2    3   4
my_tuple = (122, 222, 322, 42, 52)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[4])
# -----------------------------------------------
# oop through a tuple
my_tuple = (122, 222, 322, 42, 52)
print(my_tuple)

for i in my_tuple:
    print(i)
# -----------------------------------------------
my_tuple = (111, 111, 111, 22, 7879)
print(my_tuple.count(111))   ## 3
# -----------------------------------------------
my_tuple = (111, 111, 111, 22, 7879)
print(my_tuple.index(111))   ## 0
# -----------------------------------------------
my_tuple = (111, 111, 111, 22, 7879)
print(len(my_tuple)) #5       
# -----------------------------------------------
my_tuple = (122, 222, 322, 42, 52)
print(my_tuple[-2])   ## 42
# -----------------------------------------------



