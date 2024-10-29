"""
Description: This file includes the implementation of the Client class for our banking system.
Author: Lovedeep Singh Sidhu
Date: 13-09-2024
"""

# Importing necessary modules
from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import datetime

# Defining the Client class
class Client(Observer):
    """
    This class represents a client within the banking system.

    Attributes:
        client_number (int): A unique identifier for each client.
        first_name (str): The first name of the client.
        last_name (str): The last name of the client.
        email_address (str): The client's email address.
    """

    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str):
        """
        Initializes a new Client instance with the provided details.

        This constructor validates each input and raises errors if any field fails validation.

        Args:
            client_number (int): A unique identifier for the client.
            first_name (str): The client's first name. This cannot be empty.
            last_name (str): The client's last name. This cannot be empty.
            email_address (str): The client's email address. This must be a valid email format.

        Raises:
            ValueError: If the client_number is not an integer, or if the first or last name is empty.
            EmailNotValidError: If the provided email address is not valid.
        """
        # Ensure client_number is an integer
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self.__client_number = client_number

        # Ensure first_name is not empty after trimming whitespace
        if len(first_name.strip()) == 0:
            raise ValueError("First name cannot be blank.")
        self.__first_name = first_name.strip()

        # Ensure last_name is not empty after trimming whitespace
        if len(last_name.strip()) == 0:
            raise ValueError("Last name cannot be blank.")
        self.__last_name = last_name.strip()

        # Validate the email address and normalize it
        try:
            validated_email = validate_email(email_address)
            self.__email_address = validated_email.normalized
        except EmailNotValidError:
            # Assign a default email if the provided one is invalid
            self.__email_address = "email@gmail.com"

    @property
    def client_number(self) -> int:
        """
        Getter for the client_number attribute.

        Returns:
            int: The unique identifier of the client.
        """
        return self.__client_number

    @property
    def first_name(self) -> str:
        """
        Getter for the first_name attribute.

        Returns:
            str: The client's first name.
        """
        return self.__first_name

    @property
    def last_name(self) -> str:
        """
        Getter for the last_name attribute.

        Returns:
            str: The client's last name.
        """
        return self.__last_name

    @property
    def email_address(self) -> str:
        """
        Getter for the email_address attribute.

        Returns:
            str: The client's email address.
        """
        return self.__email_address

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the Client instance.

        The format is: {last_name}, {first_name} [{client_number}] - {email_address}

        Returns:
            str: A string that represents the client's details.
        """
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}\n"

    def update(self, message: str):
        """
        Responds to notifications from the subject.

        This method is called when the subject informs its observers of a state change.
        It prepares the subject and message for an email and sends it to the client's email address.

        Args:
            message (str): The content of the notification message.
        """
        # Create the subject and format the message
        subject = f"ALERT: Unusual Activity: {datetime.now().isoformat(timespec='minutes')}"
        message = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"
        
        # Simulate sending the email
        simulate_send_email(self.__email_address, subject, message)
