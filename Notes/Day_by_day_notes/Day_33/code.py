# Variable With Function (Normal Way)
x = 10
print(x)

def print_my_name():
    print("this is Shashant")

print_my_name()
# ----------------------------------------------
class Student:
    std_name = "Aditya"

my_obj = Student()
print(my_obj.std_name)

# ----------------------------------------
class Father:
    hotel = "Gupta Sweets"
    restaurant = "Veenu Restaurant"

my_obj = Father()

print(my_obj.restaurant)
print(my_obj.hotel)

# ---------------------------------------
class Aakansha_Bank_details:
    bank_name = "SBI"
    account_no = 11111111
    __bank_balance = 99999   # private variable
    __atm_pin = 9898         # private variable

my_obj = Aakansha_Bank_details()
print(my_obj.__atm_pin)     # ERROR
# ----------------------------------------------------
class Cricket:
    number_of_players = 11
    oneday_overs = 50
    t20_overs = 20

my_obj = Cricket()
print(my_obj.oneday_overs)
# -----------------------------------------
class Aditya:
    hotel = "Gupta Sweets"

    def aditya_assets(self):
        print("aditya assets")

my_obj = Aditya()

print(my_obj.hotel)
my_obj.aditya_assets()
# ------------------------------------

