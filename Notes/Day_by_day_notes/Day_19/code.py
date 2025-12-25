my_listt = [11,22,33,44]
print("before:", my_listt)

my_listt.append(99)
print("after:", my_listt)
#----------------------------------------------
my_listt = [11,22,33,44]
print("before:", my_listt)

my_listt.extend([33333,99999])
print("after:", my_listt)
#----------------------------------------------
# 3. insert()
my_list = [11, 22, 33, 44]
print("Before:", my_list)

my_list.insert(2, 999)   # Inserts 999 at index 2
print("After:", my_list)
#----------------------------------------------
# 4. remove()
my_list = [11, 22, 22, 33, 44]
print("Before:", my_list)

my_list.remove(22)
print("After:", my_list)
#----------------------------------------------
# 5. pop()
my_list = [11, 22, 24, 33, 44]
print("Before:", my_list)

my_list.pop(1)   # Removes element at index 1
print("After:", my_list)
#----------------------------------------------
# 6. index()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100]
print("Index of 24:", my_list.index(24))
#----------------------------------------------
# 7. count()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100]
print("Count of 100:", my_list.count(100))

#----------------------------------------------
# 8. sort()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100, 77]
print("Before:", my_list)
my_list.sort()
print("After:", my_list)
# ----------------------------------------------
# 9. reverse()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100, 77]
print("Before:", my_list)

my_list.reverse()
print("After:", my_list)

# ------------------------------------------------
# 10. copy()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100, 77]
copied_list = my_list.copy()

print("Copied list:", copied_list)

# --------------------------------------------------
# 11. clear()
my_list = [11, 22, 24, 33, 44, 100, 1000, 100, 77]
copied_list = my_list.copy()

print("Copied list:", copied_list)
print("Before:", my_list)

my_list.clear()
print("After:", my_list)
# --------------------------------------------------
