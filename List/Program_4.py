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

