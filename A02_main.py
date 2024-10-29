"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: Lovedeep Singh Sidhu
Date: 06-10-2024
"""

# 1. Import all BankAccount types using the bank_account package
#    Import date from datetime
from bank_account import *
from datetime import date, timedelta

# 2. Create an instance of a ChequingAccount with values of your choice including a balance which is below the overdraft limit.
try:
    chequing_account = ChequingAccount(666666, 1313, 900.00, date.today(), 1500.00, 0.05)
except Exception as e:
    print(e)

# 3. Print the ChequingAccount created in step 2.
print(chequing_account)
# 3b. Print the service charges amount if calculated based on the current state of the ChequingAccount created in step 2.
try:
    print(f"Calculated Service Charges: ${chequing_account.get_service_charges():.2f}")
except Exception as e:
    print(e)

print()

# 4a. Use ChequingAccount instance created in step 2 to deposit enough money into the chequing account to avoid overdraft fees.
try:
    chequing_account.deposit(900.00)
except Exception as e:
    print(e)

# 4b. Print the ChequingAccount
print(chequing_account)

# 4c. Print the service charges amount if calculated based on the current state of the ChequingAccount created in step 2.
try:
    print(f"Calculated Service Charges: ${chequing_account.get_service_charges():.2f}")
except Exception as e:
    print(e)

print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your choice including a balance which is above the minimum balance.
try:
    savings_account = SavingsAccount(555555, 1313, 5000.00, date.today(), 100.00)
except Exception as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
print(savings_account)

# 6b. Print the service charges amount if calculated based on the current state of the SavingsAccount created in step 5.
try:
    print(f"Calculated Service Charges: ${savings_account.get_service_charges():.2f}")
except Exception as e:
    print(e)

print()

# 7a. Use this SavingsAccount instance created in step 5 to withdraw enough money from the savings account to cause the balance to fall below the minimum balance.
try:
    savings_account.withdraw(2129.00)
except Exception as e:
    print(e)

# 7b. Print the SavingsAccount.
print(savings_account)

# 7c. Print the service charges amount if calculated based on the current state of the SavingsAccount created in step 5.
try:
    print(f"Calculated Service Charges: ${savings_account.get_service_charges():.2f}")
except Exception as e:
    print(e)

print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your choice including a date created within the last 10 years.
try:
    investment_account = InvestmentAccount(444444, 1313, 3600.00, date(2023, 12, 4), 3.50)
except Exception as e:
    print(e)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_account)

# 9b. Print the service charges amount if calculated based on the current state of the InvestmentAccount created in step 8.3
try:
    print(f"Calculated Service Charges: ${investment_account.get_service_charges():.2f}")
except Exception as e:
    print(e)

print()

# 10. Create an instance of an InvestmentAccount with values of your choice including a date created prior to 10 years ago.
try:
    investment_account_tenyears = InvestmentAccount(444444, 1313, 3600.00, date(2011, 12, 4), 3.50)
except Exception as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
print(investment_account_tenyears)

# 11b. Print the service charges amount if calculated based on the current state of the InvestmentAccount created in step 10.
try:
    print(f"Calculated Service Charges: ${investment_account_tenyears.get_service_charges():.2f}")
except Exception as e:
    print(e)

print("===================================================")
print()


# 12. Update the balance of each account created in steps 2, 5, 8, and 10 
# by using the withdraw method of the superclass and withdrawing the service 
# charges determined by each instance invoking the polymorphic get_service_charges method.
try:
    service_charge_chequingaccount = chequing_account.get_service_charges()
    chequing_account.withdraw(service_charge_chequingaccount)
    print(f"Withdrawn service charges from ChequingAccount: ${service_charge_chequingaccount:.2f}")
except Exception as e:
    print(e)
except ValueError as e:
    print(e)
try:
    service_charge_savingsaccount = savings_account.get_service_charges()
    savings_account.withdraw(service_charge_savingsaccount)
    print(f"Withdrawn service charges from SavingsAccount: ${service_charge_savingsaccount:.2f}")
except Exception as e:
    print(e)
except ValueError as e:
    print(e)
try:
    service_charge_investmentaccount = investment_account.get_service_charges()
    investment_account.withdraw(service_charge_investmentaccount)
    print(f"Withdrawn service charges from InvestmentAccount (created within last 10 years): ${service_charge_investmentaccount:.2f}")
except Exception as e:
    print(e)

except ValueError as e:
    print(e)
try:
    service_charge_investment_tenyears = investment_account_tenyears.get_service_charges()
    investment_account_tenyears.withdraw(service_charge_investment_tenyears)
    print(f"Withdrawn service charges from InvestmentAccount (created over 10 years ago): ${service_charge_investment_tenyears:.2f}")
except Exception as e:
    print(e)
except ValueError as e:
    print(e)
print()

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing_account)
print()
print(savings_account)
print()
print(investment_account)
print()
print(investment_account_tenyears)
print()
print("===================================================")
