from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Class Character"""
    first_name: str
    is_alive: bool

    def __init__(self, first_name, is_alive=True):
        """class Character init

        Args:
            first_name (str): character's first name
            is_alive (bool, optional): state describing if they alive or not.
            Defaults to True.
        """
        try:
            assert type(first_name) is str, 'first_name must be str'
            assert type(is_alive) is bool, 'is_alive must be bool'
            self.first_name = first_name
            self.is_alive = is_alive
        except AssertionError as error:
            raise error

    @abstractmethod
    def die(self):
        """ method that set self.is_alive to False"""
        self.is_alive = False


class Stark(Character):
    """Class Starck that inherits from Character Class"""

    def __init__(self, first_name, is_alive=True):
        """class Starck init

        Args:
            first_name (str): character's first name
            is_alive (bool, optional): state describing if they alive or not.
            Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Method that sets `is_alive` attribute to False"""
        self.is_alive = False
