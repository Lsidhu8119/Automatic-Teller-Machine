"""
Description: Unit tests for the ChequingAccount class.
Author: Lovedeep Singh Sidhu
Date: 05/10/2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_chequing_account.py
"""

import unittest
from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):

    """  
     To check the proper working of the ChequingAccount class.
    """
    
    def setUp(self):
        """Set up the initial state for each test."""
        self.chequing_account = ChequingAccount(666666, 1313, 900.00, date.today(), 1500.00, 0.05)

    def test_init_valid_input_attributes_set_correctly(self):
        """Test the method sets attributes correctly for valid inputs."""
        # Act
        account = self.chequing_account

        # Assert
        self.assertEqual(account.account_number, 666666)
        self.assertEqual(account.client_number, 1313)
        self.assertEqual(account.balance, 900.00)
        self.assertEqual(account._date_created, date.today())
        self.assertEqual(account._ChequingAccount__overdraft_limit, 1500.00)
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_init_invalid_overdraft_limit_defaults_to_negative_100(self):
        """Test to check defaults overdraft limit to -100.00 when invalid input is given."""
        # Act
        account = ChequingAccount(666666, 1313, 900.00, date.today(), "invalid_limit", 0.05)

        # Assert
        self.assertEqual(account._ChequingAccount__overdraft_limit, -100.00)

    def test_init_invalid_overdraft_rate_defaults_to_0_05(self):
        """Test to check that defaults overdraft rate to 0.05 when invalid input is given."""
        # Act
        account = ChequingAccount(666666, 1313, 900.00, date.today(), 1500.00, "invalid_rate")

        # Assert
        self.assertEqual(account._ChequingAccount__overdraft_rate, 0.05)

    def test_init_invalid_date_created_defaults_to_today(self):
        """Test to check that defaults date_created to today's date when invalid input is given."""
        # Act
        account = ChequingAccount(666666, 1313, 900.00, "invalid_date", 1500.00, 0.05)

        # Assert
        self.assertEqual(account._date_created, date.today())

    def test_get_service_charges_balance_above_overdraft_limit_returns_base_service_charge(self):
        """Test to check if the method returns base charge when balance is above the overdraft limit."""
        # Act
        account = ChequingAccount(666666, 1313, 2000.00, date.today(), 1500.00, 0.05)
        actual_value = account.get_service_charges()
        expected_value = 10.0

        # Assert
        self.assertEqual(expected_value, round(actual_value, 2))

    def test_get_service_charges_balance_below_overdraft_limit_returns_correct_service_charge(self):
        """Test to check get_service_charges calculates correctly when balance is below the overdraft limit."""
        # Act
        account = ChequingAccount(666666, 1313, -600.00, date.today(), 1500.00, 0.05)
        expected_value = (10.0 + 
                          (account._ChequingAccount__overdraft_limit - account.balance) * account._ChequingAccount__overdraft_rate)
        actual_value = account.get_service_charges()

        # Assert
        self.assertEqual(expected_value, round(actual_value, 2))

    def test_get_service_charges_balance_equals_overdraft_limit_returns_base_charge(self):
        """Test to check the method returns base charge when balance equals the overdraft limit."""
        # Act
        account = ChequingAccount(666666, 1313, 1500.00, date.today(), 1500.00, 0.05)
        actual_value = account.get_service_charges()
        expected_value = 10.0

        # Assert
        self.assertEqual(expected_value, round(actual_value, 2))

    def test_str_returns_correct_string_representation(self):
        """Test to check that str method returns the correct string representation of the account."""
        # Act
        account = ChequingAccount(666666, 1313, 900.00, date.today(), 1500.00, 0.05)
        expected_output = (
            "Account Number: 666666 Balance: $900.00\n"
            "Overdraft Limit: $1,500.00 Overdraft Rate: 5.00% Account Type: Chequing"
        )

        # Assert
        self.assertEqual(str(account), expected_output)

if __name__ == "__main__":
    unittest.main()  
