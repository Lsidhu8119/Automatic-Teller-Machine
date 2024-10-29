"""
Description: This module defines the abstract ServiceChargeStrategy class for calculating service charges.
Author: Lovedeep Singh Sidhu
"""

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    An abstract base class for defining service charge strategies applicable to bank accounts.

    Attributes:
        BASE_SERVICE_CHARGE (float): A constant representing the base service charge applicable to all accounts.

    Methods:
        calculate_service_charges(self, account: BankAccount) -> float:
            Abstract method to compute service charges based on the specific strategy.
    """

    # Constant representing the base service charge
    BASE_SERVICE_CHARGE = 10.00  

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract method to calculate service charges based on the account's balance.

        Args:
            account (BankAccount): The bank account instance for which to calculate service charges.

        Returns:
            float: The computed service charge.
        """
        pass
