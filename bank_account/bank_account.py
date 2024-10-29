"""
Description: BankAccount class representing a bank account with methods for deposit, withdrawal, and balance management.
Author: Lovedeep Singh Sidhu
"""

# Importing required modules
from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject

# Defining the BankAccount class
class BankAccount(Subject, ABC):
    """
    A class to represent a bank account.

    Attributes:
        account_number (int): Unique bank account number.
        client_number (int): Identifier for the account holder.
        balance (float): Current balance in the account.
        date_created (date): Date when the account was created.
        
    Methods:
        __init__(self, account_number, client_number, balance, date_created):
            Initializes the bank account with account number, client number, balance, and creation date.
        account_number(self) -> int:
            Returns the account number.
        client_number(self) -> int:
            Returns the client number.
        balance(self) -> float:
            Returns the current balance.
        date_created(self) -> date:
            Returns the account creation date.
        update_balance(self, amount):
            Updates the balance by adding the specified amount.
        deposit(self, amount):
            Deposits a positive amount into the account.
        withdraw(self, amount):
            Withdraws a positive amount from the account.
        get_service_charges(self) -> float:
            Abstract method for calculating service charges based on account type.
    """
    
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date):
        """
        Initialize a BankAccount object with account details.

        Args:
            account_number (int): Bank account number.
            client_number (int): Client identifier.
            balance (float): Initial account balance.
            date_created (date): Account creation date.

        Raises:
            ValueError: If account_number, client_number, or balance are invalid.
        """
        super().__init__()  # Initialize as an observer subject

        # Set account number
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account Number must be an integer.")
         
        # Set client number
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be an integer.")
        
        # Set balance
        try:
            self.__balance = float(balance)
        except ValueError:
            self.__balance = 0  # Default to zero if balance is invalid
            
        # Set account creation date
        self._date_created = date_created if isinstance(date_created, date) else date.today()

        # Define balance thresholds
        self.LOW_BALANCE_LEVEL: float = 50.0    
        self.LARGE_TRANSACTION_THRESHOLD: float = 9999.99

    # Property accessors
    @property
    def account_number(self) -> int:
        """Returns the account number."""
        return self.__account_number

    @property
    def client_number(self) -> int:
        """Returns the client number."""
        return self.__client_number

    @property
    def balance(self) -> float:
        """Returns the current balance."""
        return self.__balance

    # Balance update method
    def update_balance(self, amount):
        """
        Updates the balance by the specified amount.

        Args:
            amount (float): Amount to adjust the balance.

        Raises:
            ValueError: If amount is not a numeric value.
        """
        try:
            amount = float(amount)
            self.__balance += amount  # Adjust balance
            if self.__balance < self.LOW_BALANCE_LEVEL:
                message = f"Low balance warning ${self.__balance:.2f}: on account {self.__account_number}."
                self.notify(message)

            if amount > self.LARGE_TRANSACTION_THRESHOLD:
                message = f"Large transaction ${amount:.2f}: on account {self.__account_number}." 
                self.notify(message)

        except:
            raise ValueError(f"Amount must be numeric. Invalid value: {amount}")

    # Deposit method
    def deposit(self, amount: float):
        """
        Deposits a positive amount into the account.

        Args:
            amount (float): Amount to deposit.

        Raises:
            ValueError: If the amount is non-numeric or non-positive.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")

        self.update_balance(amount)

    # Withdraw method
    def withdraw(self, amount: float):
        """
        Withdraws a positive amount from the account.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If the amount is non-numeric, non-positive, or exceeds balance.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        
        if amount > self.__balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} exceeds balance: ${self.__balance:,.2f}")
    
        # Deduct amount
        self.update_balance(-amount)

        """
    @abstractmethod
    def get_service_charges(self) -> float:
        
        Calculate the service charges for the account.

        Returns:
            float: The calculated service charges.
        (Abstract Mrthod): To be implemented in the subclass.
        
        pass
    """

    def __str__(self) -> str:
        """Returns a string representation of the bank account."""
        return f"Account Number: {self.__account_number} Balance: ${self.__balance:,.2f}"
