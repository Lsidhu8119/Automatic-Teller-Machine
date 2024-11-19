"""
Description: This class represents an Investment Account.
Author: Lovedeep Singh Sidhu
Date: 06/10/2024
"""

from datetime import date, timedelta, datetime
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    A class that represents an Investment Account.

    Attributes:
        TEN_YEARS_AGO (date): A constant representing the date 10 years ago.
        management_fee (float): The management fee associated with the investment account.

    Methods:
        __init__(self, account_number: int, client_number: int, balance: float, date_created: date, management_fee: float):
            Initializes the InvestmentAccount with the account number, client number, balance, 
            creation date, and management fee.
        management_fee(self) -> float:
            Returns the management fee for the account.
        compute_service_charges(self) -> float:
            Calculates and returns service charges based on the account's age and management fee.
        __str__(self) -> str:
            Provides a string representation of the InvestmentAccount, including management fee details.
    """

    def __init__(self, account_number: int, client_number: int, balance: float,
                 date_created: date, management_fee: float):
        """
        Initializes the InvestmentAccount object.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client number associated with the account.
            balance (float): The initial balance of the account.
            date_created (date): The date the account was created.
            management_fee (float): The management fee for the account.

        Raises:
            ValueError: If account_number or client_number are not integers, or if balance is not a valid float.
        """
        # Define the date for 10 years ago
        self.TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

        super().__init__(account_number, client_number, balance, date_created)

        # Set the management fee
        try:
            self.__management_fee = float(management_fee)
        except ValueError:
            self.__management_fee = 2.55  # Default management fee

        self.__strategy = ManagementFeeStrategy(self._date_created, self.__management_fee)

    def __str__(self) -> str:
        """Provides a string representation of the InvestmentAccount."""
        
        # Ensure date comparison consistency
        date_created = self._date_created
        if isinstance(date_created, datetime):
            date_created = date_created.date()
            
        if date_created <= self.TEN_YEARS_AGO:
            fee = "Waived"
        else:
            fee = f"${self.__management_fee:.2f}"

        # Call the superclass's string method
        str_repr = super().__str__()

        return (f"{str_repr}\n"
                f"Date Created: {self._date_created} "
                f"Management Fee: {fee} "
                f"Account Type: Investment")

    def get_service_charges(self) -> float:
        """Calculates service charges for the InvestmentAccount.

        Returns:
            float: The calculated service charge based on account age.
        """
        return self.__strategy.calculate_service_charges(self)
