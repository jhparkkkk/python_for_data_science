from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Class Character"""

    def __init__(self, first_name, is_alive=True):
        """ class Character created"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """ method that set self.is_alive to False"""
        self.is_alive = False


class Stark(Character):
    """Class Starck that inherits from Character Class"""

    def __init__(self, first_name, is_alive=True):
        """Class Stark init"""
        super().__init__(first_name, is_alive)
        pass

    def die(self):
        """Method that sets `self.is_alive` attribute to False"""
        # print(f"{self.first_name} is dead")
        self.is_alive = False

# your code here
