"""
Description: This module contains the definition of the Observer class, which acts as a blueprint
for all observers that need to be informed about changes in the subject.
Author: Lovedeep Singh Sidhu
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    This is the Observer interface, outlining the method for receiving updates 
    regarding changes in the subject. Any concrete observer class must implement 
    this interface to handle notifications appropriately.
    """

    @abstractmethod
    def update(self, message: str):
        """
        This method gets called to notify the observer when the subject changes.
        
        Args:
            message (str): A brief description of the change that occurred.
        
        Raises:
            NotImplementedError: This exception is raised if the update method 
            is not implemented in a subclass.
        """
        pass
