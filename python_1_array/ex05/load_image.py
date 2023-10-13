from imageio.v3 import imread
from filetype import is_image
from pathlib import Path


def ft_load(path: str) -> list:
    try:
        # check if file exist
        path = Path(path)
        # check if file type is image
        assert is_image(path), "invalid image type"
        image = imread(path)
        return image
    except AssertionError as error:
        raise (error)
    except FileNotFoundError as error:
        raise (error)
    except PermissionError as error:
        raise (error)

