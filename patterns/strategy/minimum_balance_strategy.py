"""
Description: This module defines the MinimumBalanceStrategy class to calculate service charges 
based on minimum balance requirements.
Author: Lovedeep Singh Sidhu
"""

# Import necessary modules
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from bank_account.bank_account import BankAccount

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Represents the Minimum Balance Strategy for bank accounts.

    This strategy determines service charges based on whether the account balance
    falls below a specified minimum threshold.

    Attributes:
        __minimum_balance (float): The minimum balance required to avoid incurring extra service charges.
        SERVICE_CHARGE_PREMIUM (float): A constant multiplier for service charges if the balance is below the minimum.
    """
        
    def __init__(self, minimum_balance: float):
        """
        Initializes the MinimumBalanceStrategy object.

        Args:
            minimum_balance (float): The minimum balance that must be maintained in the account.
        """
        self.__minimum_balance = minimum_balance
        self.SERVICE_CHARGE_PREMIUM: float = 2.0  # Multiplier for service charge if below minimum

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charges based on the account's current balance.
        If the account's balance is less than the minimum balance, a premium service charge is applied.
        Args:
            account (BankAccount): The bank account instance for which to calculate service charges.

        Returns:
            float: The calculated service charges based on the account's balance.
        """
        # Perform the calculations
        if account.balance < self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        return self.BASE_SERVICE_CHARGE
