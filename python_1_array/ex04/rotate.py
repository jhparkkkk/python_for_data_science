import matplotlib.pyplot as plt
from load_image import ft_load
import cv2
import numpy as np
from math import radians, cos, sin
# def rotate_image(image, angle_degrees):
#     angle = radians(angle_degrees)
#     height = image.shape[0]
#     width = image.shape[1]


#     # Calculate the dimensions of the new image
#      # Calculate the dimensions of the new image
#     new_width = 400
#     new_height = 400


#     # Create an empty canvas for the rotated image
#     rotated_image = np.zeros((new_height, new_width), dtype=image.dtype)

#     # Calculate the center of the original image
#     center_x, center_y = width // 2, height // 2

#     # Calculate the center of the rotated image
#     new_center_x, new_center_y = new_width // 2, new_height // 2

#     for i in range(new_height):
#         for j in range(new_width):
#             # Calculate the original coordinates
#             x = (i - new_center_y) * cos(angle) + (j - new_center_x) * sin(angle) + center_x
#             y = -(i - new_center_y) * sin(angle) + (j - new_center_x) * cos(angle) + center_y
            
#             if 0 <= x < height and 0 <= y < width:
#                 rotated_image[i, j] = image[int(x), int(y)]

#     return rotated_image
def main():
    try:
        # Load image
        image = ft_load("animal.jpeg")
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
    print(f"The shape of image is: {crop_img.shape} or {crop_img.shape[:2]}")
    print(crop_img)
    # Transpose the 
    # rot_img = np.zeros(crop_img.shape[:2], dtype=np.float32)
    # rot_img = rotate_image(crop_img, 90)
    # rot_img = np.uint8(rot_img)
    # First we will convert the degrees into radians
    rads = radians(90)

    # We consider the rotated image to be of the same size as the original
    rot_img = np.zeros(crop_img.shape[:2])

    # Finding the center point of rotated (or original) image.
    height = rot_img.shape[0]
    width  = rot_img.shape[1]
    print('height:', height)
    print('width:', width)


    midx,midy = (width//2, height//2)
    print(f"midx:", midx)
    i = 0
    j = 0
    for i in range(height):
        
        for j in range(width):
            x = (i-midx)*abs(cos(rads))+(j-midy)*abs(sin(rads))
            y = -(i-midx)*abs(sin(rads))+(j-midy)*abs(cos(rads))

            x = round(x)+midx 
            y = round(y)+midy


            if (x>=0 and y>=0 and x<=height  and  y<width):
                rot_img[i,j] = crop_img[x,y]
            else:
                print(f"{i} and {j} | {x} and {y} ")
                rot_img[i,j] = 0
    
    print(f"New shape after Transpose: {rot_img.shape}\n{rot_img}")


    # Display the image
    plt.imshow(rot_img, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
