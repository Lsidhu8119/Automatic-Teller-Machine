"""
Description: Unit tests for the Client class.
Author: Lovedeep Singh Sidhu
Date: 28-10-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from email_validator import EmailNotValidError
from client.client import Client  

class TestClient(unittest.TestCase):
    
    def test_init_attributes_set(self):
        """Test Case 1: Ensure attributes are set to input values during initialization."""
        client = Client(99999, "Lovedeep", "Sidhu", "Lovedeepsidhu8119@gmail.com") 
        self.assertEqual(client._Client__client_number, 99999)
        self.assertEqual(client._Client__first_name, "Lovedeep")
        self.assertEqual(client._Client__last_name, "Sidhu")
        self.assertEqual(client._Client__email_address, "Lovedeepsidhu8119@gmail.com")  

    def test_init_invalid_client_number(self):
        """Test Case 2: Raise exception when an invalid client number is provided."""
        with self.assertRaises(ValueError):
            Client("invalid", "Lovedeep", "Sidhu", "Lovedeepsidhu8119@gmail.com")

    def test_init_blank_first_name(self):
        """Test Case 3: Raise exception when the first name is blank."""
        with self.assertRaises(ValueError):
            Client(99999, "   ", "Sidhu", "Lovedeepsidhu8119@gmail.com")

    def test_init_blank_last_name(self):
        """Test Case 4: Raise exception when the last name is blank.""" 
        with self.assertRaises(ValueError):
            Client(99999, "Lovedeep", "   ", "Lovedeepsidhu8119@gmail.com")

    def test_init_invalid_email(self):
        """Test Case 5: Set email address to default when an invalid email is provided."""
        client = Client(99999, "Lovedeep", "Sidhu", "invalid-email")  
        self.assertEqual(client._Client__email_address, "email@gmail.com")  

    def test_client_number_accessor(self):
        """Test Case 6: Ensure client_number property returns the correct value."""
        client = Client(99999, "Lovedeep", "Sidhu", "Lovedeepsidhu8119@gmail.com")
        self.assertEqual(client.client_number, 99999)

    def test_first_name_accessor(self):
        """Test Case 7: Ensure first_name property returns the correct value."""
        client = Client(99999, "Lovedeep", "Sidhu", "Lovedeepsidhu8119@gmail.com")
        self.assertEqual(client.first_name, "Lovedeep")

    def test_last_name_accessor(self):
        """Test Case 8: Ensure last_name property returns the correct value."""
        client = Client(99999, "Lovedeep", "Sidhu", "Lovedeepsidhu8119@gmail.com")
        self.assertEqual(client.last_name, "Sidhu")

    def test_email_address_accessor(self):
        """Test Case 9: Ensure email_address property returns the correct value."""
        client = Client(99999, "Lovedeep", "Sidhu", "Lovedeepsidhu8119@gmail.com")
        self.assertEqual(client.email_address, "Lovedeepsidhu8119@gmail.com") 

    def test_str_method(self):
        """Test Case 10: Ensure str method returns a properly formatted string."""
        client = Client(99999, "Lovedeep", "Sidhu", "Lovedeepsidhu8119@gmail.com")
        self.assertEqual(str(client), "Sidhu, Lovedeep [99999] - Lovedeepsidhu8119@gmail.com\n") 

if __name__ == "__main__":
    unittest.main()
