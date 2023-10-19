from typing import Any

# mean
# median
# quartile
# std
# var


def mean(data_list: list):
    return (sum(data_list) / len(data_list))


def median(data_list: list):
    sorted_list = sorted(data_list)
    res = sorted_list[len(sorted_list)//2]
    return res


def quartile(data_list: list):
    sorted_list = sorted(data_list)
    middle = len(sorted_list)//2
    quartiles_list = []
    quartiles_list.append(float(median(sorted_list[:middle])))
    quartiles_list.append(float(median(sorted_list[middle:])))
    return quartiles_list


def std(data_list: list):
    return var(data_list) ** (1/2)


def var(data_list: list):
    mean_value = mean(data_list)
    variance_value = 0
    for value in data_list:
        variance_value += (value - mean_value) ** 2
    variance_value /= len(data_list)
    return variance_value


def ft_statistics(*args: Any, **kwargs: Any) -> None:
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
