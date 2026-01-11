for i in range(0,5):
    print(i)
# ----------------------------------
for i in range(5):
    print(i)
# ------------------------------------
# For Loop on List (Sequence)
#              0       1       2   3   4
my_listt = ["Ravi", "rohit", 44, 55, 88]
print(my_listt)

for i in my_listt:
    print(i)
# -------------------------------------
for i in range(0, 12):
    if i == 7:
        break
    print(i)
# --------------------------------------
            #  0       1     2   3   4
my_listt = ["Ravi", "rohit", 44, 55, 88]

for i in my_listt:
    if i == 44:
        break
    print(i)
# ---------------------------------------
my_listt = ["Ravi", "rohit", 101, 44, 55, 88]

for i in my_listt:
    if i == 101:
        break
# -----------------------------------------
# continue on List
my_listt = ["Ravi", "rohit", 101, 44, 55, 88]

for i in my_listt:
    if i == 101:
        continue
    print(i)


