"""
Description: This class serves as a Subject in the observer pattern, managing
the list of observers that need to be notified of changes.
Author: Lovedeep Singh Sidhu
"""

class Subject:
    """
    The base Subject class that keeps track of observers and notifies them
    whenever there are changes in state.
    
    Attributes:
        _observers (list): A protected list containing all the observers to be notified.
    
    Methods:
        attach(observer): Adds an observer to the notification list if it isn't already present.
        detach(observer): Removes an observer from the notification list if it exists.
        notify(message): Sends a notification message to all attached observers.
    """
    
    def __init__(self):
        """Initializes the Subject with an empty list of observers."""
        self._observers = []

    def attach(self, observer):
        """
        Adds an observer to the list of observers.

        Args:
            observer: The observer instance that needs to be added.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        Removes an observer from the list of observers.

        Args:
            observer: The observer instance that needs to be removed.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        """
        Notifies all observers about a state change.

        Args:
            message (str): The message to be sent to each observer.
        """
        for observer in self._observers:
            observer.update(message)
