"""
Description: Unit tests for the SavingsAccount class.
Author: Lovedeep Singh Sidhu
Date: 05/10/2024
Usage: To run all tests in the terminal, use the following command:
    python -m unittest tests/test_savings_account.py
"""

import unittest
from bank_account.bank_account import BankAccount
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestSavingsAccount(unittest.TestCase):
    """
    This class tests the features of the SavingsAccount class.
    """

    def setUp(self):
        """Set up the environment for each test case."""
        # Create a SavingsAccount object with test data
        self.savings_account = SavingsAccount(555555, 1313, 5000.00, date.today(), 100.00)  # Updated account details

    def test_init_valid_input_attributes_set_correctly(self):
        """Check that the account is created with the right details."""
        account = self.savings_account
        self.assertEqual(account.account_number, 555555)  # Updated account number
        self.assertEqual(account.client_number, 1313)
        self.assertEqual(account.balance, 5000.00)  # Updated balance
        self.assertEqual(account._date_created, date.today())  # Check creation date
        self.assertEqual(account._SavingsAccount__minimum_balance, 100.00)  # Updated minimum balance

    def test_init_invalid_minimum_balance_defaults_to_50(self):
        """Verify that an invalid minimum balance sets it to the default value of 50.00."""
        # Create an account with an invalid minimum balance
        account = SavingsAccount(555555, 1313, 5000.00, date.today(), "invalid")  # Updated account details
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.00)  # Default minimum balance

    def test_get_service_charges_balance_above_minimum_returns_base_service_charge(self):
        """Check if the service charge is the base amount when the balance is above the minimum."""
        account = SavingsAccount(555555, 1313, 5000.00, date.today(), 100.00)  # Updated account details
        actual_value = account.get_service_charges()
        expected_value = 10.0  # Expected base service charge
        self.assertEqual(expected_value, round(actual_value, 2))  # Verify the charge

    def test_get_service_charges_balance_equal_to_minimum_returns_base_service_charge(self):
        """Check if the service charge remains the base amount when the balance equals the minimum."""
        account = SavingsAccount(555555, 1313, 100.00, date.today(), 100.00)  # Updated account details
        actual_value = account.get_service_charges()
        expected_value = 10.0  # Expected base service charge
        self.assertEqual(expected_value, round(actual_value, 2))  # Verify the charge

    def test_get_service_charges_balance_below_minimum_returns_premium_charge(self):
        """Check that a premium charge is applied when the balance falls below the minimum."""
        account = SavingsAccount(555555, 1313, 50.00, date.today(), 100.00)  # Updated account details
        actual_value = account.get_service_charges()
        expected_value = 10.0 * 2.0  # Expected premium service charge
        self.assertEqual(expected_value, round(actual_value, 2))  # Verify the charge

    def test_str_returns_correct_string_representation(self):
        """Check if the string representation of the account is formatted correctly."""
        account = SavingsAccount(555555, 1313, 5000.00, date.today(), 100.00)  # Updated account details
        expected_output = (
            "Account Number: 555555 Balance: $5,000.00\n"  # Updated account number
            "Minimum Balance: $100.00 Account Type: Savings"
        )
        self.assertEqual(str(account), expected_output)  # Verify the string output

if __name__ == "__main__":
    unittest.main()  # This runs all the tests
