from S1E9 import Character
from colorama import Fore


class Baratheon(Character):
    """Representing the Baratheon family."""
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def __init__(self, first_name, is_alive=True, family_name="Baratheon", eyes="brown", hairs="dark"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def die(self):
        """Method that sets `self.is_alive` attribute to False"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"

    def __init__(self, first_name, is_alive=True, family_name="Lannister", eyes="blue", hairs="light"):
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def create_lannister(first_name: str, is_alive: bool):
        return Lannister(first_name, is_alive)

    def die(self):
        """Method that sets `self.is_alive` attribute to False"""
        self.is_alive = False
