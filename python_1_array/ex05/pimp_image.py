from numpy import ndarray, empty_like, round


def ft_invert(array: ndarray) -> ndarray:
    """Inverts the color of the image received.
    """
    rows, cols, depth = array.shape
    result = empty_like(array)
    for r in range(rows):
        for c in range(cols):
            for d in range(depth):
                value = array[r, c, d]
                result[r, c, d] = 255 - value
    print(f"The shape of image is: {result.shape}\n{result}")
    return result


# #your code here
def ft_red(array: ndarray) -> ndarray:
    """Fiters the green and blue colors of the image received
to render a red image.
    """
    result = empty_like(array)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            # R
            result[i, j, 0] = array[i, j, 0]
            # G
            result[i, j, 1] *= 0
            # B
            result[i, j, 2] *= 0
    print(f"The shape of image is: {result.shape}\n{result}")
    return result


# #your code here
def ft_green(array: ndarray) -> ndarray:
    """Fiters the red and blue colors of the image received
to render a green image.
    """
    result = empty_like(array)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            # R
            result[i, j, 0] = array[i, j, 0] - array[i, j, 0]
            # G
            result[i, j, 1] = array[i, j, 1]
            # B
            result[i, j, 2] = array[i, j, 2] - array[i, j, 2]
    print(f"The shape of image is: {result.shape}\n{result}")
    return result


# #your code here
def ft_blue(array: ndarray) -> ndarray:
    """Fiters the red and green colors of the image received
to render a blue image.
    """
    result = empty_like(array)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            # R
            result[i, j, 0] = 0
            # G
            result[i, j, 1] = 0
            # B
            result[i, j, 2] = array[i, j, 2]
    print(f"The shape of image is: {result.shape}\n{result}")
    return result
# #your code here


def ft_grey(array: ndarray) -> ndarray:
    """Lower intensity of each color space to render
a grayscaled image.
    """
    result = empty_like(array)
    result = result.astype('float')
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            intensity = (array[i, j, 0] / 02.99 + array[i, j,
                         1] / 05.87 + array[i, j, 2] / 01.14) / 1.2
            # R
            result[i, j, 0] = intensity
            # G
            result[i, j, 1] = intensity
            # B
            result[i, j, 2] = intensity
    result = round(result).astype('int')
    print(f"The shape of image is: {result.shape}\n{result}")
    return result
