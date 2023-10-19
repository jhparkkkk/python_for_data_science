from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """class King derived from superclass Baratheon and Lannister

    Args:
        Baratheon (Character): class derived from Character class
        Lannister (Character): class derived from Character class
    """

    def __init__(self, first_name, is_alive=True):
        """King class init

        Args:
            first_name (str): character's first name
            is_alive (bool, optional): state describing if they alive or not. \
Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_eyes):
        """set eyes attribut

        Args:
            new_eyes (str): to update eyes' attribute
        """
        try:
            assert type(new_eyes) is str, 'eyes must be str'
            self.eyes = new_eyes
        except AssertionError as error:
            raise error

    def set_hairs(self, new_hairs):
        """set hairs attribut

        Args:
            new_hairs (str): to update hairs' attribute
        """
        try:
            assert type(new_hairs) is str, 'hairs must be str'
            self.hairs = new_hairs
        except AssertionError as error:
            raise error

    def get_eyes(self):
        """return eyes attribute's value

        Returns:
            str: character's eyes' color
        """
        return self.eyes

    def get_hairs(self):
        """return hairs attribute's value

        Returns:
            str: character's hairs' color
        """
        return self.hairs
