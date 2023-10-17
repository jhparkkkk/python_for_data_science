import pandas as pd


def load(path: str) -> pd.core.frame.DataFrame:
    """Loads data from .csv file writes the dimensions of the data set
and returns it

    Args:
        path (str): .csv file
    Returns:
        pd.core.frame.DataFrame: pandas dataframe
    """
    try:
        # load .csv as dataframe
        assert path.endswith('.csv'), "not a csv file"
        dataframe = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataframe.shape}")
        return dataframe
    except AssertionError as error:
        print(f"Invalid file: {error}")
    except Exception as error:
        print(f"CSV file not valid: {error}")
        return None
    except FileNotFoundError as error:
        print(error)
        return None
