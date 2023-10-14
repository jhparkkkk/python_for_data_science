from numpy import shape


def slice_me(family: list, start: int, end: int) -> list:
    """
    slice a list sequence from `start` to `end`

    Args:
        family (list): sequence to slice
        start (int): where the slicing starts
        end (int): where the slicing ends

    Returns:
        list: the sliced list
    """
    try:
        assert type(family) is list, "sequence is not a list"
        assert len(family) != 0, "list is empty"
        assert all([type(row) is list for row in family]), \
            "subsequent sequences are not all lists"
        assert all([len(row) == len(family[0]) for row in family]), \
            "subsequent lists are not the same size"

        print(f"My shape is : {shape(family)}")
        sliced_family = family[start:end]
        print(f"My new shape is : {shape(sliced_family)}")
        return sliced_family
    except AssertionError as assertion_error:
        print(f"AssertionError:{assertion_error}")
        return None
