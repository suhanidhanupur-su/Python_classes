Day: 42:- 
What is Encapsulation?
Encapsulation means hiding important/sensitive data and allowing access to it only through specific methods.
It helps in:
Data security
Controlled access
Better code structure


Real Life Example (Concept Understanding)
Encapsulation is like a medicine capsule:
Medicine is hidden inside the capsule
You cannot see or directly touch the medicine
You can only consume it in a controlled way



Access Specifiers in Python
There are three types of access specifiers used in encapsulation:
Public
Protected (_)
Private (__)
1. Public Access Specifier
Accessible from anywhere
No underscore used


class Shivam:
    shivam_bank_name = "SBI"
    shivam_account_type = "Salary Account"

shivam_obj = Shivam()
print(shivam_obj.shivam_bank_name)


📌 Public members are not secure.

2. Protected Access Specifier (_)
Represented using a single underscore _
Should be accessed inside class or child class
Still accessible, but not recommended outside


class Shivam:
    _shivam_account_no = 78979379

shivam_obj = Shivam()
print(shivam_obj._shivam_account_no)


📌 Protected members are partially hidden.

3. Private Access Specifier (__)
Represented using double underscore __
Cannot be accessed directly outside the class
Used for highly sensitive data


class Shivam:
    __shivam_atm_pin = 8989

# shivam_obj = Shivam()
# # print(shivam_obj.__shivam_atm_pin)  # ERROR

# 📌 Private members are fully hidden.

# Accessing Private Data Using Methods (Correct Way)
class Shivam:
    shivam_bank_name = "SBI"
    shivam_account_name = "Salary Account"
    _shivam_account_no = 78979379      # Protected
    __shivam_bank_balance = 200000     # Private
    __shivam_atm_pin = 8989            # Private

    def shivam_bank_info(self):
        print("Bank Name:", self.shivam_bank_name)
        print("Account Type:", self.shivam_account_name)
        print("Account Number:", self._shivam_account_no)
        print("Bank Balance:", self.__shivam_bank_balance)

shivam_obj = Shivam()
shivam_obj.shivam_bank_info()


# Output
# Bank Name: SBI
# Account Type: Salary Account
# Account Number: 78979379
# Bank Balance: 200000



