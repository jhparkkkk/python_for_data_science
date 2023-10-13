import matplotlib.pyplot as plt
from load_image import ft_load
import cv2
import numpy as np


def main():
    try:
        # Load image
        image = ft_load("animal.jpeg")
        print(image)
    except FileNotFoundError as error:
        print(error)
        exit(1)
    # Convert the color image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # slice
    start_x = 100
    start_y = 450
    end_x = start_x + 400
    end_y = start_y + 400
    # Crop the image
    crop_img = gray_image[start_x:end_x, start_y:end_y, np.newaxis]
    print(f"New shape after slicing:{crop_img.shape} or {crop_img.shape[:2]}")
    print(crop_img)
    # Display the grayscale image
    plt.imshow(crop_img, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
