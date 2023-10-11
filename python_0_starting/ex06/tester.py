from ft_filter import ft_filter
from colorama import Fore


def is_even(x):
    return x % 2 == 0


def is_exoplanet(name):
    exoplanets = \
        ("Kepler-186f", "TrES-2b", "WASP-39b", "HD209458b", "Gliese 581g")
    return name in exoplanets


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["WASP-39b", "toto", "HD209458b", "titi"]
# ---------------------------------------------------------------------------
#   My own ft_filter
# ---------------------------------------------------------------------------
print(Fore.LIGHTCYAN_EX, "\n----------- my ft_filter -------------\n")
my_filter = ft_filter(is_even, numbers)
ft_filtered_elements = list(my_filter)
print(ft_filtered_elements)  # Output: [2, 4, 6, 8, 10]
print(ft_filter.__doc__)
print(ft_filter.__name__)
filter_planets = ft_filter(is_exoplanet, names)
filtered_elements = list(filter_planets)
print(filtered_elements)


# ---------------------------------------------------------------------------
#   Original filter
# ---------------------------------------------------------------------------
print(Fore.LIGHTMAGENTA_EX, "\n----------- original filter -------------\n")
original_filter = filter(is_even, numbers)
filtered_elements = list(original_filter)
print(filtered_elements)
print(filter.__doc__)
print(filter.__name__)
filter_planets = filter(is_exoplanet, names)
filtered_elements = list(filter_planets)
print(filtered_elements)
