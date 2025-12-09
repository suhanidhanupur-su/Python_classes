# 🗳️ Program 3: Voting Eligibility in Bihar
my_age = int(input("Hii, Ujwal! Enter your age: "))
residence = input("Do you live in Bihar? (yes/no): ").lower()

if my_age >= 18 and residence == 'yes':
    print("You are eligible to vote in Bihar.")
else:
    print("You are not eligible to vote in Bihar.")

