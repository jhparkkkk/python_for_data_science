from load_image import ft_load


def test_mandatory():
    """mandatory tests given by the subject
    """
    print(ft_load("landscape.jpg"))
    print(ft_load("animal.jpeg"))
    # print(ft_load("landscape.png"))
    # print(ft_load("landscape.txt"))
    # print(ft_load("landscape.jpeg"))
    # print(ft_load("landscape.gif"))


if __name__ == "__main__":
    test_mandatory()
