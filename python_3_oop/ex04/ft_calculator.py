class calculator:
    """class used to do calculations of 2 vectors:
dot product, addition, substraction
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        method to operate dot product
        a · b = ax × bx + ay × by

        Args:
            V1 (list[float]): first vector
            V2 (list[float]): second vector
        """
        if len(V1) != len(V2):
            print('cannot operate: vectors are not the same size')
            return
        new_vec = [value_v1 * value_v2 for value_v1, value_v2 in zip(V1, V2)]
        res = 0
        for value in new_vec:
            res += value
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        method to operate addition between 2 vector

        Args:
            V1 (list[float]): first vector
            V2 (list[float]): second vector
        """
        if len(V1) != len(V2):
            print('cannot operate: vectors are not the same size')
            return
        new_vec = [float(value_v1) + float(value_v2) for value_v1,
                   value_v2 in zip(V1, V2)]
        print(f"Add Vector is : {new_vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        method to operate substraction between 2 vector

        Args:
            V1 (list[float]): first vector
            V2 (list[float]): second vector
        """
        if len(V1) != len(V2):
            print('cannot operate: vectors are not the same size')
            return
        new_vec = [float(value_v1) - float(value_v2) for value_v1,
                   value_v2 in zip(V1, V2)]
        print(f"Sous Vector is : {new_vec}")
