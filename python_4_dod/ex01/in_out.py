

def square(x: int | float) -> int | float:
    """Calculate the square of the given value

    Args:
        x (int | float): the given value

    Returns:
        int | float: the squared of the given value
    """
    res = x * x
    return res


def pow(x: int | float) -> int | float:
    """Calculate the exponentiation of the given value

    Args:
        x (int | float): the given value

    Returns:
        int | float: the exponentiated value
    """
    res = x ** x
    return res


def outer(x: int | float, function) -> object:
    """Calculate the square or the exponentation
of the given value

    Args:
        x (int | float): the given value
        function (function): the function to call

    Returns:
        object: result of the inner function
    """
    count = 0
    count = x

    def inner() -> float:
        nonlocal count
        res = function(count)
        count = res
        return res

    return inner
