from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    family_name = "Baratheon"
    eyes = "brown"
    hairs = "dark"

    def __init__(self, first_name, is_alive=True,
                 family_name="Baratheon", eyes="brown", hairs="dark"):
        """Baratheon class init

        Args:
            first_name (str): character's first name
            is_alive (bool, optional): state describing if alive or not. \
            Defaults to True.
            family_name (str, optional): character's family name. \
            Defaults to "Baratheon".
            eyes (str, optional): character's eyes' color. \
            Defaults to "brown".
            hairs (str, optional): character's hairs' color. \
            Defaults to "dark".


        Raises:
            error: if params are invalid types
        """
        super().__init__(first_name, is_alive)
        try:
            assert type(family_name) is str, 'family_name must be str'
            assert type(eyes) is str, 'eyes must be str'
            assert type(hairs) is str, 'hairs must be str'
            self.family_name = family_name
            self.eyes = eyes
            self.hairs = hairs
        except AssertionError as error:
            raise error

    def __str__(self):
        """returns a string describing character's
family name, eye color and hair color.

        Returns:
            str: string representation of an object
        """
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """returns a string describing character's family name,
eye color and hair color.

        Returns:
            str: string representation of an object
        """
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def die(self):
        """Method that sets `self.is_alive` attribute to False"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""
    family_name = "Lannister"
    eyes = "blue"
    hairs = "light"

    def __init__(self, first_name, is_alive=True,
                 family_name="Lannister", eyes="blue", hairs="light"):
        """Lannister class init

        Args:
            first_name (str): character's first name
            is_alive (bool, optional): state describing if they alive or not. \
            Defaults to True.
            family_name (str, optional): character's family name. \
            Defaults to "Lannister".
            eyes (str, optional): character's eyes' color. \
            Defaults to "blue".
            hairs (str, optional): character's hairs' color. \
            Defaults to "light".

        Raises:
            error: if params are invalid types
        """
        super().__init__(first_name, is_alive)
        try:
            assert type(family_name) is str, 'family_name must be str'
            assert type(eyes) is str, 'eyes must be str'
            assert type(hairs) is str, 'hairs must be str'
            self.family_name = family_name
            self.eyes = eyes
            self.hairs = hairs
        except AssertionError as error:
            raise error

    def __str__(self):
        """Returns a string describing character's family name,
eye color and hair color.

        Returns:
            str: string representation of an object
        """
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """Returns a string describing character's family name,
eye color and hair color.

        Returns:
            str: string representation of an object
        """
        return f"Vector: {self.family_name, self.eyes, self.hairs}"

    def create_lannister(first_name: str, is_alive: bool):
        """Create a character Lannister by instantiating class Lannister.

        Args:
            first_name (str): character's first name
            is_alive (bool): if alive or not

        Returns:
            Lannister : class object that has been instantiated.
        """
        return Lannister(first_name, is_alive)

    def die(self):
        """Method that sets `self.is_alive` attribute to False"""
        self.is_alive = False
