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
        assert path.endswith('.csv'), "not a csv file"
        dataframe = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataframe.shape}")
        return dataframe
    except AssertionError as error:
        raise (error)
    except Exception as error:
        raise (error)
    except FileNotFoundError as error:
        raise (error)
