"""
Description: This class is responsible for displaying the details of a bank account and facilitating bank account transactions such as deposits and withdrawals.
Author: Lovedeep Singh Sidhu
"""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated = Signal(BankAccount)  # Define a signal to send the updated account object

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the AccountDetailsWindow.
        Args:
            account: The bank account to be displayed.
        """
        super().__init__()

        # Validate that the account parameter is of type BankAccount
        if isinstance(account, BankAccount):
            # Create a copy of the account to avoid modifying the original directly
            self.account = copy.copy(account)
            # Populate the window's labels with account information
            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            # Connect buttons to their respective methods
            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)

        else:
            # If the account is not valid, close the window
            QMessageBox.warning(self, "Invalid Account", "The provided account is not valid.")
            self.reject()

    def on_apply_transaction(self) -> None:
        """
        Handles the deposit or withdrawal transactions based on user input.
        """
        try:
            # Get the transaction amount input from the user and convert to float
            amount = float(self.transaction_amount_edit.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Transaction amount must be a valid number.")
            self.transaction_amount_edit.setFocus()
            return

        # Ensure that the amount is positive
        if amount <= 0:
            QMessageBox.warning(self, "Invalid Amount", "Amount must be greater than zero.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            # Determine which button triggered the event
            if self.sender() == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)
            elif self.sender() == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)

            # Update the balance label after the transaction
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            # Emit the balance_updated signal to update any listeners (ClientLookupWindow)
            self.balance_updated.emit(self.account)

            # Clear the input field and set focus back to it
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

        except Exception as e:
            # Handle any exceptions raised during the transaction
            QMessageBox.warning(self, f"{transaction_type} Failed", f"{transaction_type} failed: {str(e)}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    def on_exit(self) -> None:
        """
        Closes the account details window and returns to the previous window.
        """
        self.close()
