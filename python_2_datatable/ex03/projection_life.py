import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import ScalarFormatter


def get_year_data(dataframe: pd.core.frame.DataFrame,
                  year: str) -> pd.core.frame.DataFrame:
    """retrieve  a specific year-column

    Args:
        dataframe (pd.core.frame.DataFrame): dataframe to filter
        year (str): column to filter out

    Returns:
        pd.core.frame.DataFrame: filtered dataframe
    """
    try:
        df_one_year = dataframe[['country', '1900']]
        return df_one_year
    except Exception as error:
        raise error


def thousand(x, pos) -> int:
    """convert thousands to `xK`

    Args:
        x (int): value
        pos (None): position
    Returns:
        int: converted value
    """
    if x % 10000 == 0:
        return f'{str(x)[:2]}K'
    elif x % 1000 == 0:
        return f'{str(x)[:1]}K'
    return x


def main():
    try:
        df_life_expectancy = load('life_expectancy_years.csv')
        df_income_per_person = load(
            'income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
        df_life_expectancy = get_year_data(df_life_expectancy, '1900')
        df_income_per_person = get_year_data(df_income_per_person, '1900')
    except Exception as error:
        print(f"An error occurred: {error}")
        exit(1)

    fig1, ax1 = plt.subplots()
    ax1.set_xscale('log')
    ax1.set_xticks([300, 1000, 10000])
    ax1.get_xaxis().set_major_formatter(ScalarFormatter())
    plt.scatter(x=df_income_per_person['1900'], y=df_life_expectancy['1900'])
    plt.xticks([300, 1000, 10000])
    formatter = FuncFormatter(thousand)
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life expectancy')
    plt.show()


if __name__ == "__main__":
    main()
