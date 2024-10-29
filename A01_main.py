"""
Description: A client program written to verify the correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: Lovedeep Singh Sidhu
Date: 13-09-2024
"""
from bank_account.bank_account import BankAccount
from client.client import Client
 
def main():
    """Test the functionality of the methods encapsulated
    in the BankAccount and Client classes.
    """
    # Print statement to clarify the output in the terminal
    print("\nStarting the BankAccount and Client functionality tests.\n")
 
    # 1. Create a valid instance of the Client class.
    try:
        client_information = Client(99999, "Lovedeep", "Sidhu", "lovedeepsidhu8119@gmail.com")
        print("Client created successfully:", client_information)
    except ValueError as e:
        print("Error creating Client:", e)
 
    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None
 
    # 3. Instantiate the BankAccount object.
    try:
        bank_account = BankAccount(81199, 99999, 1500.00)
        print("BankAccount created successfully:", bank_account)
    except ValueError as e:
        print("Error creating BankAccount:", e)
 
    # 4. Attempt to create an instance of the BankAccount class with an invalid balance.
    try:
        invalid_account = BankAccount(81200, 99999, "Invalid Balance")
    except ValueError as e:
        print("Error creating BankAccount with invalid balance:", e)
 
    # 5. Print the Client instance created.
    # Print the BankAccount instance created in step 3.
    print("\nClient information:", client_information)
    print("BankAccount information:", bank_account)
 
    # 6. Attempt to deposit a non-numeric value into the BankAccount.
    try:
        bank_account.deposit("invalid_deposit")
    except ValueError as e:
        print("\nError in depositing non-numeric value:", e)
 
    # 7. Attempt to deposit a negative value into the BankAccount.
    try:
        bank_account.deposit(-500.00)
    except ValueError as e:
        print("Error in depositing negative value:", e)
 
    # 8. Attempt to withdraw a valid amount from the BankAccount.
    try:
        bank_account.withdraw(200.00)
        print("\nValid withdraw made successfully. Updated balance:", bank_account.balance)
    except ValueError as e:
        print("Error in withdrawing valid amount:", e)
 
    # 9. Attempt to withdraw a non-numeric value from the BankAccount.
    try:
        bank_account.withdraw("invalid_withdraw")
    except ValueError as e:
        print("Error in withdrawing non-numeric value:", e)
 
    # 10. Attempt to withdraw a negative value from the BankAccount.
    try:
        bank_account.withdraw(-300.00)
    except ValueError as e:
        print("Error in withdrawing negative value:", e)
 
    # 11. Attempt to withdraw a value that exceeds the current balance of the account.
    try:
        bank_account.withdraw(2000.00)
    except ValueError as e:
        print("Error in withdrawing amount exceeding balance:", e)
 
    # 12. Print the final BankAccount statement.
    print("\nFinal Bank Statement:", bank_account)
 
if __name__ == "__main__":
    main()
