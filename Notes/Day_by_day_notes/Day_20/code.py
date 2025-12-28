i = 0

while (i < 5):
    print(i)
    i += 1
# -------------------------------------------------
# PROGRAM 1 — Print 1 to 6 using While Loop
i = 1
while(i < 7):
    print(i)
    i = i + 1
#---------------------------------------------------

# PROGRAM 2 — Even–Odd Check
a = 15
if(a % 2 == 0):
    print("Even Num =", a)
else:
    print("Odd Number =", a)
# ----------------------------------------------------
# PROGRAM 3 — Print Even Numbers From 1 to 99
i = 1
while(i < 100):
    if(i % 2 == 0):
        print(i)
    i = i + 1
# -----------------------------------------------------
# PROGRAM 4 — Print Even Numbers From User Input to 99
i = int(input("Hii Ujjwal Enter Value Of i = "))
while(i < 100):
    if(i % 2 == 0):
        print(i)
    i = i + 1
# -----------------------------------------------------
# PROGRAM 5 — Even Numbers Between Start & End (User Input)
i = int(input("Hii Ujjwal Enter Value Of Stating Point = "))
ending_point = int(input("Enter The Value Of Ending Point = "))

while(i < ending_point):
    if(i % 2 == 0):
        print(i)
    i = i + 1

