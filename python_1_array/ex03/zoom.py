from load_image import ft_load
from cv2 import cvtColor, COLOR_BGR2GRAY
from numpy import newaxis
from matplotlib.pyplot import imshow, show


def main():
    """
    crop an image to zoom in.
    Display information about the cropped image:
    - The size in pixel on both X and Y axis
    - The number of channel
    - The pixel content of the image.
    - Display the scale on the x and y axis on the image
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
    # Display the image
    imshow(crop_img, cmap="gray")
    show()


if __name__ == "__main__":
    main()
