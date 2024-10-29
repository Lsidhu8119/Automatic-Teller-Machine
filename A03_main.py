"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: Lovedeep Singh Sidhu
Date: 27-10-2024
"""

# Import all necessary classes from the bank_account and client packages
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from datetime import date
from client.client import Client

def main():
    # Step 2: Create a Client object with updated personal information
    client1 = Client(1313, "Lovedeep", "Sidhu", "sidhulovedeep8119.com")  # Updated client information

    # Step 3a: Create a ChequingAccount object for the first client
    chequing_account_object = ChequingAccount(
        account_number=666666,         # Updated unique account number
        client_number=client1.client_number,  # Associate with the updated client
        balance=900.00,               # Initial balance
        date_created=date.today(),    # Account creation date
        overdraft_limit=1500.00,      # Allowed overdraft limit
        overdraft_rate=0.05           # Overdraft interest rate
    )

    # Step 3b: Create a SavingsAccount object for the first client
    savings_account_object = SavingsAccount(
        account_number=555555,         # Updated unique account number
        client_number=client1.client_number,  # Associate with the updated client
        balance=5000.00,              # Initial balance
        date_created=date.today(),     # Account creation date
        minimum_balance=100.00         # Minimum required balance
    )

    # Step 4: Attach the Client object as an observer to the account objects
    chequing_account_object.attach(client1)
    savings_account_object.attach(client1)

    # Step 5a: Create a second Client object with different information
    client2 = Client(2002, "Ramandeep", "Kaur", "Ramandeepkaur@gmail.com")

    # Step 5b: Create a SavingsAccount object for the second client
    savings_account_object2 = SavingsAccount(
        account_number=13579,        # Unique account number for the second client
        client_number=client2.client_number,  # Associate with the second client
        balance=3000.00,             # Initial balance
        date_created=date.today(),    # Account creation date
        minimum_balance=30.00        # Minimum required balance
    )

    # Step 6: Perform transactions that may notify observers
    transactions = [
        (chequing_account_object, "deposit", 80000.00),  # Large deposit to chequing account
        (savings_account_object, "withdraw", 600.00),    # Withdrawal from savings account (may drop below minimum)
        (chequing_account_object, "deposit", 65000.00),  # Another large deposit
        (savings_account_object2, "withdraw", 900.00)     # Withdrawal from second savings account
    ]

    # Execute each transaction and handle any exceptions
    for account, action, amount in transactions:
        try:
            if action == "deposit":
                account.deposit(amount)  # Perform deposit
            elif action == "withdraw":
                account.withdraw(amount)  # Perform withdrawal
        except Exception as e:
            # Print error message if a transaction fails
            print(f"Error in {action} for account {account.account_number}: {e}")

# Entry point of the program
if __name__ == "__main__":
    main()
