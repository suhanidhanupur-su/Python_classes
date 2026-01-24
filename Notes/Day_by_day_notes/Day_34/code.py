class Father:
    father_property = "Bhardwaj Empire"

class Son:
    son_property = "Mohit Pan Dukan"

son_obj = Son()

print(son_obj.son_property)
# print(son_obj.father_property)   # ERROR
# ==============================================

class Father:
    father_property = "Bhardwaj Empire"

class Son(Father):
    son_property = "Mohit Pan Dukan"

son_obj = Son()

print(son_obj.son_property)
print(son_obj.father_property)
# ================================================
class Company:
    cmp_name = "TCS"
    number_of_emp = 600

    def comp_info(self):
        print("It's all about this company")

my_obj = Company()

print(my_obj.cmp_name)
my_obj.comp_info()

# =================================================
class Virat_Kohli:
    jersey_no = 18
    bat_brand = "MRF"

virat_obj = Virat_Kohli()
print(virat_obj.jersey_no)


