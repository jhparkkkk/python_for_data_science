from typing import Any


def callLimit(limit: int):
    """Limit function calling by counting it.
If limit is reached print error

    Args:
        limit (int): limit of calling function

    Returns:
        function(*arg, *kwds): the called function
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count, limit
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, *kwds)
        return limit_function
    return callLimiter
