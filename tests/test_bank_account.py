"""
Description: Unit tests for the BankAccount class.
Author: Lovedeep Singh Sidhu
Date: 13-09-2024
Usage: To execute all tests in the terminal, run the command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_init_attributes_set(self):
        """Test 1: Check that the account is initialized with the correct values."""
        account = BankAccount(81199, 99999, 1500.0)
        self.assertEqual(account._BankAccount__account_number, 81199)
        self.assertEqual(account._BankAccount__client_number, 99999)
        self.assertEqual(round(account._BankAccount__balance, 2), 1500.0)

    def test_init_non_numeric_balance(self):
        """Test 2: Ensure the balance defaults to 0 if a non-numeric value is given."""
        account = BankAccount(81199, 99999, "invalid")
        self.assertEqual(round(account._BankAccount__balance, 2), 0.0)

    def test_init_invalid_account_number(self):
        """Test 3: Verify that a ValueError is raised for a non-numeric account number."""
        with self.assertRaises(ValueError):
            BankAccount("invalid", 99999, 1500.0)

    def test_init_invalid_client_number(self):
        """Test 4: Verify that a ValueError is raised for a non-numeric client number."""
        with self.assertRaises(ValueError):
            BankAccount(81199, "invalid", 1500.0)

    def test_account_number_getter(self):
        """Test 5: Check that the account_number property returns the correct value."""
        account = BankAccount(81199, 99999, 1500.0)
        self.assertEqual(account.account_number, 81199)

    def test_client_number_getter(self):
        """Test 6: Ensure the client_number property returns the expected value."""
        account = BankAccount(81199, 99999, 1500.0)
        self.assertEqual(account.client_number, 99999)

    def test_balance_getter(self):
        """Test 7: Make sure the balance property returns the correct balance."""
        account = BankAccount(81199, 99999, 1500.0)
        self.assertEqual(round(account.balance, 2), 1500.0)

    def test_update_balance_positive_amount(self):
        """Test 8: Check that updating balance with a positive amount works correctly."""
        account = BankAccount(81199, 99999, 100.0)
        account.update_balance(50.0)
        self.assertEqual(round(account._BankAccount__balance, 2), 150.0)

    def test_update_balance_negative_amount(self):
        """Test 9: Ensure that updating balance with a negative amount works as expected."""
        account = BankAccount(81199, 99999, 100.0)
        account.update_balance(-50.0)
        self.assertEqual(round(account._BankAccount__balance, 2), 50.0)

    def test_update_balance_non_numeric_amount(self):
        """Test 10: Check that the balance remains unchanged when a non-numeric amount is passed."""
        account = BankAccount(81199, 99999, 100.0)
        account.update_balance("invalid")
        self.assertEqual(round(account._BankAccount__balance, 2), 100.0)

    def test_deposit_valid_amount(self):
        """Test 11: Verify that depositing a valid amount updates the balance correctly."""
        account = BankAccount(81199, 99999, 100.0)
        account.deposit(50.0)
        self.assertEqual(round(account._BankAccount__balance, 2), 150.0)

    def test_deposit_negative_amount(self):
        """Test 12: Ensure that depositing a negative amount raises a ValueError."""
        account = BankAccount(81199, 99999, 100.0)
        with self.assertRaises(ValueError):
            account.deposit(-50.0)

    def test_withdraw_valid_amount(self):
        """Test 13: Check that withdrawing a valid amount updates the balance correctly."""
        account = BankAccount(81199, 99999, 100.0)
        account.withdraw(50.0)
        self.assertEqual(round(account._BankAccount__balance, 2), 50.0)

    def test_withdraw_negative_amount(self):
        """Test 14: Ensure that trying to withdraw a negative amount raises a ValueError."""
        account = BankAccount(81199, 99999, 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(-50.0)

    def test_withdraw_exceeds_balance(self):
        """Test 15: Check that withdrawing more than the available balance raises a ValueError."""
        account = BankAccount(81199, 99999, 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(150.0)

    def test_str_method(self):
        """Test 16: Ensure the string representation of the account is formatted correctly."""
        account = BankAccount(81199, 99999, 500.0)
        self.assertEqual(str(account), "Account Number: 81199 Balance: $500.00\n")


if __name__ == '__main__':
    unittest.main()
