import pathlib as pathlib
import pandas as pd

def load(path: str) -> pd.core.frame.DataFrame:
    try:
        # load .csv as dataframe 
        dataframe = pd.read_csv(path)
        print(dataframe.shape)
        return dataframe
    except Exception as error:
        print(f"CSV file not valid: {error}")
    except FileNotFoundError as error:
        print(error)