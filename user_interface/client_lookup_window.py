 
"""
Description: This class defines the ClientLookupWindow, a user interface for looking up clients and their associated bank accounts. 
Author: Lovedeep Singh Sidhu
"""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    def __init__(self):
        super().__init__()
        # Load data for clients and accounts
        self.client_listing, self.accounts = load_data()

        # Connect buttons and events
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.account_table.cellClicked.connect(self.on_select_account)

    @Slot()
    def on_lookup_client(self):
        """Handles the lookup button click event to find and display client information."""
        try:
            # Obtain and validate client number from input
            client_number = int(self.client_number_edit.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Client number must be numeric.")
            self.reset_display()
            return

        # Check if the client exists
        if client_number not in self.client_listing:
            QMessageBox.warning(self, "Client Not Found", f"Client number {client_number} does not exist.")
            self.reset_display()
            return

        # Display client information
        client = self.client_listing[client_number]
        self.client_info_label.setText(f"{client.first_name} {client.last_name}")

        # Display associated bank accounts
        self.account_table.setRowCount(0)  # Clear previous table entries
        for account in self.accounts.values():
            if account.client_number == client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                # Populate table cells with account information
                self.account_table.setItem(row_position, 0, QTableWidgetItem(str(account.account_number)))
                self.account_table.setItem(row_position, 1, QTableWidgetItem(f"${account.balance:,.2f}"))
                self.account_table.setItem(row_position, 2, QTableWidgetItem(str(account.date_created) if hasattr(account, 'date_created') else "N/A"))
                self.account_table.setItem(row_position, 3, QTableWidgetItem(account.__class__.__name__))

        self.account_table.resizeColumnsToContents()

    @Slot(int, int)
    def on_select_account(self, row: int, column: int):
        """Handles the cell click event to display account details."""
        # Retrieve the account number from the selected row
        account_number_item = self.account_table.item(row, 0)
        if not account_number_item:
            QMessageBox.warning(self, "Invalid Selection", "No account selected.")
            return

        # Ensure the account number exists in the accounts dictionary
        account_number = int(account_number_item.text())
        if account_number not in self.accounts:
            QMessageBox.warning(self, "Error", "Bank account does not exist.")
            return

        # Open the Account Details window
        account = self.accounts[account_number]
        details_window = AccountDetailsWindow(account)

        # Connect the balance_updated signal from AccountDetailsWindow to the update_data method
        details_window.balance_updated.connect(self.update_data)

        details_window.exec_()

    @Slot(BankAccount)
    def update_data(self, account: BankAccount):
        """Updates the account table and data after receiving the balance_updated signal."""
        # Loop through the rows in the account_table
        for row in range(self.account_table.rowCount()):
            account_number_item = self.account_table.item(row, 0)
            if account_number_item and int(account_number_item.text()) == account.account_number:
                # Update the balance column with the new balance
                self.account_table.setItem(row, 1, QTableWidgetItem(f"${account.balance:,.2f}"))

                # Update the account in the dictionary
                self.accounts[account.account_number] = account

                # Update the data in the manage_data module
                update_data(account)
                break
