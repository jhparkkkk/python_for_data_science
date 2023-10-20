from typing import Any


def mean(data_list: list) -> int | float:
    """calculate average of a given list of numbers
    mean = (sum of observations) ÷ (total number of observations)
    Args:
        data_list (list): data set to operate on

    Returns:
        int | float: means of the data set passed as parameters
    """
    return (sum(data_list) / len(data_list))


def median(data_list: list) -> int | float:
    """Calculates the middle value of the given data set.
    Median = {(n + 1) / 2}th

    Args:
        data_list (list): data set to operate on

    Returns:
        int | float: the middle value
    """
    sorted_list = sorted(data_list)
    res = sorted_list[len(sorted_list)//2]
    return res


def quartile(data_list: list) -> list[float]:
    """Calculate the values that separate the data into four equal parts

    Args:
        data_list (list): data set to operate on

    Returns:
        list[int | float]: list containing first quartile and third quartile
    """

    sorted_list = sorted(data_list)
    middle = len(sorted_list)//2
    quartiles_list = []
    quartiles_list.append(float(median(sorted_list[:middle])))
    quartiles_list.append(float(median(sorted_list[middle:])))
    return quartiles_list


def std(data_list: list) -> float:
    """Calculate the standard deviation : describe the variation
of data points meaning
    how close they are to the mean.

    Args:
        data_list (list): data set to operate on

    Returns:
        float: the standard deviation value
    """
    return var(data_list) ** (1/2)


def var(data_list: list) -> float:
    """Calculate the variance ofthe given data.
A large variance indicates that the data is spread out

    Args:
        data_list (list): data set to operate on

    Returns:
        float: the variance value
    """
    mean_value = mean(data_list)
    variance_value = 0
    for value in data_list:
        variance_value += (value - mean_value) ** 2
    variance_value /= len(data_list)
    return variance_value


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """make the Mean, Median,
Quartile (25% and 75%), Standard Deviation and Variance
according to the **kwargs
    """
    statistics_dict = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var,
    }
    data_list = []
    try:
        for arg in args:
            assert type(arg) is int or type(
                arg) is float, f"value {arg} is not int"
            data_list.append(arg)

        for key, value in kwargs.items():
            if len(data_list) != 0:
                if value in statistics_dict:
                    print(f"{value}: {statistics_dict[value](data_list)}")
            else:
                print("ERROR")

    except AssertionError as error:
        print(error)
