from load_image import ft_load
from pimp_image import ft_invert
import matplotlib.pyplot as plt
...
array = ft_load("landscape.jpg")

print(type(array))
inverted_color = ft_invert(array)
# ft_red(array)
# ft_green(array)
# ft_blue(array)
# ft_grey(array)
# print(ft_invert.__doc__)

plt.imshow(inverted_color)
plt.show()