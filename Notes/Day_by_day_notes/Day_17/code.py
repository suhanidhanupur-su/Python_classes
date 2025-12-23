for(int i = 0; i < 5; i++){
    printf("%d", i);
}
# ---------------------------------------------
# 1. Basic Range
for i in range(5):
    print("first output", i)
# ---------------------------------------------
# 2. Range (0,5)
for i in range(0,5):
    print("second output", i)
# ---------------------------------------------
# 3. Range (13,18)
for i in range(13,18):
    print(i)
    # ----------------------------------------------
# 4. Range (22,27)
for i in range(22,27):
    print(i)
# ------------------------------------------------
# 5. Slicing Example
listt = [22,21,23,33,44,55]
print(listt[0:3])
# --------------------------------------------------
6. Gap Example
print(listt[0:5:2])
# --------------------------------------------------
7. Even Numbers
for i in range(2,21,2):
    print(i)
# --------------------------------------------------
# 8. Multiples of 5
for i in range(5,51,5):
    print(i)

# --------------------------------------------------
# 9. Negative to Positive
for i in range(-2,5):
    print(i)

# --------------------------------------------------
# 10. Your last example
for i in range(9,23,1):
    print("first output", i)

for i in range(9,23):
    print("second output", i)



