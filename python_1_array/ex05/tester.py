from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt

from mpl_toolkits.axes_grid1 import ImageGrid
array = ft_load("landscape.jpg")

print(type(array))
inverted_color = ft_invert(array)
red_filtered = ft_red(array)
green_filtered = ft_green(array)
blue_filtered = ft_blue(array)
grey_filtered = ft_grey(array)
# print(ft_invert.__doc__)

# plt.imshow(inverted_color)
fig = plt.figure(figsize=(10., 10.))
grid = ImageGrid(fig, 111,
                 nrows_ncols=(3, 2),
                 axes_pad=0.2,
                 )

for ax, im in zip(grid, [array, inverted_color, red_filtered, green_filtered, blue_filtered, grey_filtered]):
    ax.imshow(im)

plt.show()
