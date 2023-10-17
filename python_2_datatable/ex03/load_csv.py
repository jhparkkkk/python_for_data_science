import pathlib as pathlib
import pandas as pd
import seaborn as sns


def load(path: str) -> pd.core.frame.DataFrame:
    try:
        dataframe = pd.read_csv(path)
        print(dataframe.shape)

        return dataframe
    except Exception as error:
        raise (error)
    except FileNotFoundError as error:
        raise (error)
