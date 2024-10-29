"""
Description: This module defines the OverdraftStrategy class for calculating service charges 
related to overdraft.
Author: Lovedeep Singh Sidhu
"""

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    This class implements the overdraft service charge strategy, which extends the ServiceChargeStrategy.

    Attributes:
        overdraft_limit (float): The maximum amount the account can be overdrawn.
        overdraft_rate (float): The fee rate applied when the account is overdrawn.

    Methods:
        __init__(self, overdraft_limit: float, overdraft_rate: float):
            Sets up the overdraft strategy with a defined limit and rate.
        calculate_service_charges(self, account: BankAccount) -> float:
            Computes service charges based on the account's overdraft status.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the OverdraftStrategy object.

        Args:
            overdraft_limit (float): The limit for overdrawing the account.
            overdraft_rate (float): The fee rate applied to overdrafts.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charges based on the current overdraft status of the account.

        Args:
            account (BankAccount): The bank account instance to assess for service charges.

        Returns:
            float: The computed service charge based on the account's overdraft situation.
        """
        # Start with the base service charge defined in the ServiceChargeStrategy class
        base_service_charge = self.BASE_SERVICE_CHARGE

        # Determine if the account balance is within the overdraft limit
        if account.balance >= self.__overdraft_limit:
            return base_service_charge
        else:
            # Calculate the charge incurred due to the overdraft
            return (base_service_charge +
                    (self.__overdraft_limit - account.balance) * self.__overdraft_rate)
