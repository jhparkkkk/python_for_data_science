from colorama import Fore


class calculator:
    vector = []

    def __init__(self, vector: list):
        self.vector = vector

    def __add__(self, object) -> None:
        new_vec = list(map(lambda value: value + object, self.vector))
        self.vector = new_vec
        print(self.vector)

    def __mul__(self, object) -> None:
        new_vec = list(map(lambda value: value * object, self.vector))
        self.vector = new_vec
        print(self.vector)

    def __sub__(self, object) -> None:
        new_vec = list(map(lambda value: value - object, self.vector))
        self.vector = new_vec
        print(self.vector)

    def __truediv__(self, object) -> None:
        if object == 0:
            print('cannot divide by zero')
            return
        new_vec = list(map(lambda value: value / object, self.vector))
        self.vector = new_vec
        print(self.vector)
