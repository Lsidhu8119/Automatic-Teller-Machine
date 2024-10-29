"""
Description: Unit tests for the InvestmentAccount class.
Author: Lovedeep Singh Sidhu
Date: 28-10-2024
Usage: To run all tests in the terminal, use 
the following command:
    python -m unittest tests/test_investment_account.py
"""

import unittest
from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta

class TestInvestmentAccount(unittest.TestCase):
    """
    This class tests the InvestmentAccount class.
    """

    def setUp(self):
        """Prepare a fresh InvestmentAccount for each test."""
        # Create an InvestmentAccount object with test data
        self.account = InvestmentAccount(444444, 1313, 3600.00, date(2023, 12, 4), 3.50)  # Updated account details

    def test_init_valid_input_attributes_set_correctly(self):
        """Check if the account is created with the right details."""
        # Get the account details
        account_number = self.account.account_number
        client_number = self.account.client_number
        balance = self.account.balance
        date_created = self.account._date_created
        management_fee = self.account._InvestmentAccount__management_fee

        # Verify the account details are correct
        self.assertEqual(account_number, 444444)  
        self.assertEqual(client_number, 1313)
        self.assertEqual(balance, 3600.00)  
        self.assertEqual(date_created, date(2023, 12, 4))  
        self.assertEqual(management_fee, 3.50)

    def test_init_invalid_management_fee_returns_default_management_fee(self):
        """Check if an invalid management fee sets the fee to the default value."""
        # Create an account with an invalid management fee
        account = InvestmentAccount(444444, 1313, 3600.00, date(2023, 12, 4), "invalid_fee")  
        management_fee = account._InvestmentAccount__management_fee

        # Verify that the management fee is set to the default
        self.assertEqual(management_fee, 2.55)

    def test_get_service_charges_account_created_more_than_10_years_ago_returns_base_charges(self):
        """Check if service charges are waived for accounts older than 10 years."""
        # Create an account that was created over 10 years ago
        account = InvestmentAccount(444444, 1313, 3600.00, date.today() - timedelta(days=11 * 365.25), 3.50)  
        actual_value = account.get_service_charges()

        # Verify that the expected service charge is returned
        expected_value = 10.0
        self.assertEqual(expected_value, round(actual_value, 2))

    def test_get_service_charges_account_created_exactly_10_years_ago_returns_base_charges(self):
        """Check service charges when the account was created exactly 10 years ago."""
        # Create an account that was created exactly 10 years ago
        account = InvestmentAccount(444444, 1313, 3600.00, date.today() - timedelta(days=10 * 365.25), 3.50)  
        actual_value = account.get_service_charges()

        # Verify that the expected service charge is returned
        expected_value = 13.5
        self.assertEqual(expected_value, round(actual_value, 2))

    def test_get_service_charges_account_created_less_than_10_years_ago_apply_management_fee(self):
        """Check service charges for accounts created less than 10 years ago."""
        # Create an account that was created less than 10 years ago
        account = InvestmentAccount(444444, 1313, 3600.00, date.today() - timedelta(days=5 * 365.25), 3.50) 
        actual_value = account.get_service_charges()

        # Verify that the expected service charge is returned
        expected_value = 13.5
        self.assertEqual(expected_value, round(actual_value, 2))

    def test_str_representation_account_older_than_10_years(self):
        """Check the string representation of the account when older than 10 years."""
        # Create an account older than 10 years
        account = InvestmentAccount(444444, 1313, 3600.00, date.today() - timedelta(days=11 * 365.25), 3.50) 
        actual_str = str(account)

        # Verify the string output is correct
        expected_str = ("Account Number: 444444 Balance: $3,600.00\n"  
                        f"Date Created: {account._date_created} Management Fee: Waived Account Type: Investment")
        self.assertEqual(actual_str, expected_str)

    def test_str_representation_account_less_than_10_years_old(self):
        """Check the string representation of the account when less than 10 years old."""
        # Create an account less than 10 years old
        account = InvestmentAccount(444444, 1313, 3600.00, date.today() - timedelta(days=9 * 365.25), 3.50)  
        actual_str = str(account)

        # Verify the string output is correct
        expected_str = ("Account Number: 444444 Balance: $3,600.00\n"  
                        f"Date Created: {account._date_created} Management Fee: $3.50 Account Type: Investment")
        self.assertEqual(actual_str, expected_str)

if __name__ == "__main__":
    unittest.main()  
