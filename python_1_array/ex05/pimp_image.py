from numpy import ndarray, empty_like
def ft_invert(array: ndarray) -> ndarray:
    print(type(array))

    # Get the shape of the 3D array
    depth, rows, cols = array.shape
    result = empty_like(array)

    # Iterate through the 3D array using nested loops
    for d in range(depth):
        for r in range(rows):
            for c in range(cols):
                value = array[d, r, c]
                # print(f"Element at depth {d}, row {r}, column {c} is {value}")
                result[d, r, c] = 255 - value
    
    return result


# #your code here
# def ft_red(array) -> array:
# #your code here
# def ft_green(array) -> array:
# #your code here
# def ft_blue(array) -> array:
# #your code here
# def ft_grey(array) -> array