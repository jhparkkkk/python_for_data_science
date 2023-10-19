class calculator:
    """class used for scaling vectors
    """
    vector = []

    def __init__(self, vector: list):
        """class Calculator init

        Args:
            vector (list): list of values to operate on
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """add object to each values in self.vector

        Args:
            object (int): scalar value
        """

        new_vec = [value + object for value in self.vector]
        self.vector = new_vec
        print(self.vector)

    def __mul__(self, object) -> None:
        """multiply object to each values in self.vector

        Args:
            object (int): scalar value
        """
        new_vec = [value * object for value in self.vector]

        self.vector = new_vec
        print(self.vector)

    def __sub__(self, object) -> None:
        """substract object to each values in self.vector

        Args:
            object (int): scalar value
        """
        new_vec = [value - object for value in self.vector]

        self.vector = new_vec
        print(self.vector)

    def __truediv__(self, object) -> None:
        """divide object to each values in self.vector

        Args:
            object (int): scalar value
        """
        if object == 0:
            print('cannot divide by zero')
            return
        new_vec = [value / object for value in self.vector]
        self.vector = new_vec
        print(self.vector)
