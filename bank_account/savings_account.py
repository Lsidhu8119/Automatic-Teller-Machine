"""
Description: This class models a Savings Account that extends the BankAccount functionality.
Author: Lovedeep Singh Sidhu
Date: 06/10/2024
"""

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    This class represents a Savings Account, enhancing the BankAccount class with specific features.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float): A constant that denotes the premium service charge multiplier.
        minimum_balance (float): The minimum amount required in the account to avoid extra service charges.

    Methods:
        __init__(self, account_number: int, client_number: int, balance: float, minimum_balance: float):
            Initializes a SavingsAccount with the specified account number, client number, balance, and minimum balance.
        __str__(self) -> str:
            Returns a string representation of the SavingsAccount, highlighting the minimum balance requirements.
        compute_service_charges(self) -> float:
            Computes and returns service charges based on the current balance in relation to the minimum balance.
    """

    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date, minimum_balance: float):
        """
        Sets up the SavingsAccount instance.

        Args:
            account_number (int): The unique number assigned to this bank account.
            client_number (int): The unique identifier for the client associated with the account.
            balance (float): The starting balance for this account.
            minimum_balance (float): The least amount that must be maintained in the account.
                If conversion fails, defaults to 50.00.

        Raises:
            ValueError: If account_number or client_number are not integers.
        """
        # Initialize the base class with the given parameters
        super().__init__(account_number, client_number, balance, date_created)

        # Validate and set the minimum balance
        try:
            self.__minimum_balance = float(minimum_balance)
        except ValueError:
            self.__minimum_balance = 50.00  # Assign a default value if the conversion fails

        # Set up the strategy for managing minimum balance service charges
        self.__strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def __str__(self) -> str:
        """Returns a detailed string representation of the SavingsAccount."""
        return (f"{super().__str__()}\n"
                f"Minimum Balance: ${self.__minimum_balance:.2f} "
                f"Account Type: Savings")

    def get_service_charges(self) -> float:
        """Calculates the service charges applicable to the SavingsAccount.

        Returns:
            float: The determined service charge based on the current balance and minimum balance.
        """
        return self.__strategy.calculate_service_charges(self)
