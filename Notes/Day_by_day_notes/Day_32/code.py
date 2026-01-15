def student_info():
    std_name = "Shivam"   # Local Variable
    print("here is the student information")
    print("inside this function:", std_name)

student_info()
# ----------------------------------------------------
default_std_name = "Ujwal"   # Global variable

def student_info():
    std_name = "Shivam"      # Local variable
    print("inside function global:", default_std_name)
    print("inside function local:", std_name)

student_info()
print("outside function:", default_std_name)
# ------------------------------------------------------
class Student:
    std_name = "Aditya"
    std_roll = "111"

my_obj = Student()

print(my_obj.std_name)
print(my_obj.std_roll)
# ------------------------------------------
class Student:
    def student_info(self):
        print("here is all about student info")

our_obj = Student()
our_obj.student_info()
