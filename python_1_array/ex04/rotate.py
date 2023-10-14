from load_image import ft_load
from cv2 import cvtColor, COLOR_BGR2GRAY
from numpy import newaxis, zeros, indices, round, abs
from math import radians, cos, sin
from matplotlib.pyplot import imshow, show


def main():
    """
    Crop an image and then transpose it by 90 degrees.
Display the new image and print new image's data : shape and values
    """
    try:
        # Load image
        image = ft_load("animal.jpeg")
        print(image)
    except Exception as error:
        print(f"An error occurred: {error}")
        exit(1)
    # Convert the chromatic image to grayscale
    gray_image = cvtColor(image, COLOR_BGR2GRAY)
    # slice
    start_x = 100
    start_y = 450
    end_x = start_x + 400
    end_y = start_y + 400
    # Crop the image
    crop_img = gray_image[start_x:end_x, start_y:end_y, newaxis]
    print(f"New shape after slicing:{crop_img.shape} or {crop_img.shape[:2]}")
    print(crop_img)
    # Transpose
    rads = radians(-90)
    # transposed image is here the same size as crop_img
    rot_img = zeros(crop_img.shape[:2])

    # Finding the center point of rotated (or original) image.
    height = rot_img.shape[0]
    width = rot_img.shape[1]

    midx, midy = (width//2, height//2)
    # Create arrays of indices
    i, j = indices(rot_img.shape[:2])

    # Calculate the new indices (after transpose)
    # rotation
    x = (i - midx) * abs(cos(rads)) + (j - midy) * abs(sin(rads))
    y = -(i - midx) * abs(sin(rads)) + (j - midy) * abs(cos(rads))
    # translation
    x = round(x).astype(int) + midx
    y = round(y).astype(int) + midy

    # check if x and y are inside array
    valid_indices = (x >= 0) & (y >= 0) & (x < height) & (y < width)

    # Flatten indices -> 2d to 1d
    flat_indices = x[valid_indices] * width + y[valid_indices]

    # Assign values with flattend indices
    rot_img[i[valid_indices], j[valid_indices]] = crop_img.ravel()[
        flat_indices]

    print(f"New shape after Transpose: {rot_img.shape}\n{rot_img}")

    # Display the image
    imshow(rot_img, cmap="gray")
    show()


if __name__ == "__main__":
    main()
