class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        new_vec = list(
            map(lambda value_v1, value_v2: value_v1 * value_v2, V1, V2))
        print(sum(new_vec))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        new_vec = list(
            map(lambda value_v1, value_v2: float(value_v1) + float(value_v2), V1, V2))
        print(new_vec)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        new_vec = list(
            map(lambda value_v1, value_v2: float(value_v1) - float(value_v2), V1, V2))
        print(new_vec)
