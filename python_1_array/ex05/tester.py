from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt
...
array = ft_load("landscape.jpg")

print(type(array))
# inverted_color = ft_invert(array)
# red_filtered = ft_red(array)
# green_filtered = ft_green(array)
# blue_filtered = ft_blue(array)
grey_filtered = ft_grey(array)
# print(ft_invert.__doc__)

# plt.imshow(inverted_color)
plt.imshow(grey_filtered)  # Use "gray" colormap for grayscale images

plt.show()