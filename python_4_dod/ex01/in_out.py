from colorama import Fore


def square(x: int | float) -> int | float:
    res = x * x
    return res


def pow(x: int | float) -> int | float:
    res = x ** x
    return res


def outer(x: int | float, function) -> object:
    count = 0
    count = x

    def inner() -> float:
        nonlocal count
        res = function(count)
        count = res
        return res

    return inner
