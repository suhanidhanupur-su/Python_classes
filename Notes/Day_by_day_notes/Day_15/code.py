my_number = 777

if (my_number < 500):
     print("bhai ye print hone chahiye agr condition true hai to")
else:
     print("bhai ye print hone chahiye agr condition false hai to")

    #  NOTE#: we can keep our condition in parenthesis () but it is not mandatory in python.

# -----------------------------------------------------------------------
if (n % 2 == 0):
  print(" this is even number ")

else:
 print(" this is odd number " )

# -------------------------------------------------------------------------
# 🧮 Program 1: Check if number is Positive or Negative
my_number = int(input("Hii, Suhani! Enter your favorite number: "))

if my_number > 0:
    print("Your favorite number is positive.")
else:
    print("Your favorite number is negative.")
# -------------------------------------------------------------------------
# 🔢 Program 2: Check Even or Odd Number
my_number = int(input("Hii, Suhani! Enter your favorite number: "))

if my_number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
# --------------------------------------------------------------------
# 🗳️ Program 3: Voting Eligibility in Bihar
my_age = int(input("Hii, Ujwal! Enter your age: "))
residence = input("Do you live in Bihar? (yes/no): ").lower()

if my_age >= 18 and residence == 'yes':
    print("You are eligible to vote in Bihar.")
else:
    print("You are not eligible to vote in Bihar.")
# --------------------------------------------------------------------
# 🧠 Program 4: Rohit’s Class Attendance
rohit_status = input("When did Rohit reach the class? ").lower()

if rohit_status == "on time":
    print("Rohit will attend all the lectures.")
elif rohit_status == "just after first lecture":
    print("Rohit will attend the rest of the lectures.")
elif rohit_status == "after lunch":
    print("Rohit will attend a few lectures only.")
elif rohit_status == "before class ends":
    print("Rohit will attend the last lecture only.")
else:
    print("Rohit will not attend any lectures.")
# -------------------------------------------------------------------
# 🏫 Program 5: Student Grading System
your_score = int(input("Enter your score (0-100): "))
if your_score >= 90:
    print("Grade: A")
if your_score >= 65:
    print("Grade: B")
if your_score >= 55:
    print("Grade: C")
else:
    print("Grade: F")
print("Thank you for using the grading system.")