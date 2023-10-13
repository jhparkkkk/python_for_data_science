
from imageio.v3 import imread, immeta
from filetype import is_image
from pathlib import Path
from stat import S_IRUSR
from os import access, R_OK


def ft_load(path: str) -> list:
    try:
        # check if file exist
        path = Path(path)
        # check if file type is image
        assert is_image(path), "invalid image type"
        im = imread(path)
        print(f"The shape of image is: {im.shape}")
        image = imread(path)

        metadata = immeta(path)
        print(metadata["mode"])  # "RGB"
        return image
    except AssertionError as error:
        print(f"AssertionError:{error}")
    except FileNotFoundError as error:
        print(f"FileNotFoundError:{error}")
    except PermissionError as error:
        print(f"PermissionError:{error}")
