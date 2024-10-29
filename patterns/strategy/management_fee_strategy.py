"""
Description: This module implements a strategy for managing fees in investment accounts based on account age.
Author: Lovedeep Singh Sidhu
"""

from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta
from bank_account.bank_account import BankAccount

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Represents the Management Fee Strategy applicable to Investment Accounts.

    Attributes:
        management_fee (float): The fee charged for managing the investment account.
        TEN_YEARS_AGO (date): A constant representing the date that marks 10 years ago.

    Methods:
        __init__(self, date_created: date, management_fee: float):
            Initializes the strategy with the account creation date and management fee.
        calculate_service_charges(self, account: BankAccount) -> float:
            Computes the service charges based on the age of the account and the management fee.
    """

    # Constant that determines the date from 10 years ago
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Sets up the ManagementFeeStrategy with necessary parameters.

        Args:
            date_created (date): The date the account was created.
            management_fee (float): The fee for managing the investment account.
        """
        self.__management_fee = management_fee
        self.__date_created = date_created  

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charges for the investment account.

        If the account has been active for more than 10 years, the management fee is waived.

        Args:
            account (BankAccount): The investment account for which to calculate the charges.

        Returns:
            float: The total service charge applicable.
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
