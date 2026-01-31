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