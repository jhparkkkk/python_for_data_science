import matplotlib.pyplot as plt
from load_csv import load
import numpy as np
import pandas as pd
from colorama import Fore
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import ScalarFormatter


def get_year_data(dataframe: pd.core.frame.DataFrame, year: str) -> pd.core.frame.DataFrame:
    df_one_year = dataframe[['country', '1900']]
    print(df_one_year)
    return df_one_year


def main():
    try:
        df_life_expectancy = load('life_expectancy_years.csv')
        df_income_per_person = load(
            'income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    except Exception as error:
        print(f"An error occurred: {error}")
        exit(1)

    # filter out France's data
    print(df_life_expectancy)
    print(df_income_per_person)
    df_life_expectancy = get_year_data(df_life_expectancy, '1900')
    df_income_per_person = get_year_data(df_income_per_person, '1900')
    fig1, ax1 = plt.subplots()
    ax1.set_xscale('log')
    ax1.set_xticks([300, 1000, 10000])
    ax1.get_xaxis().set_major_formatter(ScalarFormatter())
    plt.scatter(x=df_income_per_person['1900'], y=df_life_expectancy['1900'])
    plt.xticks([300, 1000, 10000])

    def thousand(x, pos):
        if x % 10000 == 0:
            return f'{str(x)[:2]}K'
        elif x % 1000 == 0:
            return f'{str(x)[:1]}K'
        return x
    formatter = FuncFormatter(thousand)
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.show()


if __name__ == "__main__":
    main()
