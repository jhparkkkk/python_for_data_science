from numpy import ndarray, empty_like, round


def ft_invert(array: ndarray) -> ndarray:
    print(type(array))

    # Get the shape of the 3D array
    depth, rows, cols = array.shape
    result = empty_like(array)
    print(f"dephth: {depth}")
    # Iterate through the 3D array using nested loops
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                value = array[d, r, c]
                # print(f"Element at depth {d}, row {r}, column {c} is {value}")
                result[d, r, c] = 255 - value

    return result


# #your code here
def ft_red(array: ndarray) -> ndarray:
    rows, cols, depth = array.shape
    result = empty_like(array)
    print(f"depth:{depth}, rows:{rows}, cols:{cols}")
  # Iterate through the 3D array using nested loops
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            # Set the red color channel in the result to the original value
            result[i, j, 0] = array[i, j, 0]
            # Set the green and blue channels in the result to 0 to remove them
            result[i, j, 1] *= 0
            result[i, j, 2] *= 0

    return result


# #your code here
def ft_green(array: ndarray) -> ndarray:
    rows, cols, depth = array.shape
    result = empty_like(array)
    print(f"depth:{depth}, rows:{rows}, cols:{cols}")
  # Iterate through the 3D array using nested loops
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            # Set the red color channel in the result to the original value
            result[i, j, 0] = array[i, j, 0] - array[i, j, 0]
            # Set the green and blue channels in the result to 0 to remove them
            result[i, j, 1] = array[i, j, 1]
            result[i, j, 2] = array[i, j, 2] - array[i, j, 2]

    return result


# #your code here
def ft_blue(array: ndarray) -> ndarray:
    rows, cols, depth = array.shape
    result = empty_like(array)
    print(f"depth:{depth}, rows:{rows}, cols:{cols}")
  # Iterate through the 3D array using nested loops
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            # Set the red color channel in the result to the original value
            result[i, j, 0] = 0
            # Set the green and blue channels in the result to 0 to remove them
            result[i, j, 1] = 0
            result[i, j, 2] = array[i, j, 2]

    return result
# #your code here


def ft_grey(array: ndarray) -> ndarray:
    rows, cols, depth = array.shape
    result = empty_like(array)
    result = result.astype('float')
    print(f"depth:{depth}, rows:{rows}, cols:{cols}")
  # Iterate through the 3D array using nested loops
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
           # Calculate the grayscale intensity as the average of the color channels
            intensity = (array[i, j, 0] / 02.99 + array[i, j,
                         1] / 05.87 + array[i, j, 2] / 01.14) / 1.2
            result[i, j, 0] = intensity
            result[i, j, 1] = intensity
            result[i, j, 2] = intensity
    result = round(result).astype('int')

    return result
