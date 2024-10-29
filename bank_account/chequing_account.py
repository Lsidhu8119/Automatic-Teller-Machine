"""
Description: The ChequingAccount class represents a bank account for transactions, featuring an overdraft limit and rate to manage account balances effectively.
Author: Lovedeep Singh Sidhu
"""
from bank_account.bank_account import BankAccount 
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    A class to represent a Chequing Account, which extends the BankAccount class.

    Attributes:
        overdraft_limit (float): The maximum amount the balance can be overdrawn.
        overdraft_rate (float): The interest rate applied on overdraft amounts.

    Methods:
        __init__(self, account_number: int, client_number: int, balance: float, date_created: date, 
                 overdraft_limit: float, overdraft_rate: float):
            Initializes the ChequingAccount with the account number, client number, initial balance, 
            creation date, overdraft limit, and overdraft rate.
        overdraft_limit(self) -> float:
            Returns the overdraft limit.
        overdraft_rate(self) -> float:
            Returns the overdraft rate.
        compute_service_charges(self) -> float:
            Calculates and returns service charges based on the overdraft status.
        __str__(self) -> str:
            Provides a string representation of the ChequingAccount, including overdraft details.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the ChequingAccount object.

        Args: 
            account_number (int): The bank account number.
            client_number (int): The client number associated with the account.
            balance (float): The initial balance of the account.
            date_created (date): The creation date of the account.
            overdraft_limit (float): The overdraft limit for this account.
            overdraft_rate (float): The overdraft interest rate.

        Raises:
            ValueError: If account_number or client_number are not integers, or if balance is not a valid float.
        """
        # superclass constructer
        super().__init__(account_number, client_number, balance, date_created)

        # Set the overdraft limit
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except ValueError:
            self.__overdraft_limit = -100.00  # Default value for overdraft limit
        
        # Set the overdraft rate
        if isinstance(overdraft_rate, (int, float)):
            self.__overdraft_rate = float(overdraft_rate)
        else:
            self.__overdraft_rate = 0.05  # Default overdraft rate

        self.__strategy = OverdraftStrategy(self.__overdraft_limit, self.__overdraft_rate)

    def __str__(self) -> str:
        """Provides a string representation of the ChequingAccount."""
        base_str = super().__str__()
        return (f"{base_str}\n"
                f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.__overdraft_rate * 100:.2f}% "
                f"Account Type: Chequing")

    def get_service_charges(self) -> float:
        """Calculates the service charges for the ChequingAccount.

        Returns:
            float: The calculated service charge based on overdraft status.
        """
        # when balance is more than overdraft limit
        return self.__strategy.calculate_service_charges(self)
