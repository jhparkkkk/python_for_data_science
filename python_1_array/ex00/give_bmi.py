import numpy as np


def is_int_or_float(value) -> bool:
    return isinstance(value, (int, float))


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    take 2 lists of integers or floats in input and returns a list
    of BMI values.

    BMI = 	mass (kg) / height * height (m)

    Args:
        height (list[int  |  float]): list of height(kg) values
        weight (list[int  |  float]): list of weight(m) values

    Returns:
        list[int | float]: a list of resulted BMI values
    """
    try:
        assert len(height) == len(weight), "weight list and height list \
            are not the same size"
        bmi_results = []
        for weight_value, height_value in zip(weight, height):
            assert is_int_or_float(weight_value), "value must be int or float"
            assert is_int_or_float(height_value), "value must be int or float"
            bmi_results.append(weight_value / np.square(height_value))
        return bmi_results
    except AssertionError as assertion_error:
        print(f"AssertionError: {assertion_error}\n")
        return None


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        for value in bmi:
            assert is_int_or_float(value), "value must be int or float"
        assert isinstance(limit, int), "limit must be int"
        return list(map(lambda value: value <= limit, bmi))
    except AssertionError as assertion_error:
        print(f"AssertionError: {assertion_error}\n")
