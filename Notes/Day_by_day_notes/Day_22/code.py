my_set = {11, 22, 33, 44, 55, 11, 22, 33}
print("this is actual elements of this set :", my_set)

# -----------------------------------------------------------
#adding method:
my_set = {11, 22, 33, 55, 44, 2}
print("before adding element :", my_set)

my_set.add(77)
print("after adding element  :", my_set)
# ------------------------------------------------------------
# 2. update()
my_set = {11, 22, 33, 55, 44, 2}
print("before adding element :", my_set)

my_set.update({77, 999, 102})
print("after adding element  :", my_set)
# -----------------------------------------------------------
# 3. remove()
my_set = {11, 22, 33, 55, 44, 2}
print("before removing element :", my_set)

my_set.remove(22)
print("after removing element  :", my_set)
# ------------------------------------------------------------
# Loop Through a Set
my_set = {11, 22, 33, "rahul", "ravi", 8.8}
print("before iteration :", my_set)

for i in my_set:
    print(i)

