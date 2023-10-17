import matplotlib.pyplot as plt
from load_csv import load
import numpy as np
import pandas as pd
from colorama import Fore
from matplotlib.ticker import FuncFormatter


def get_country_data(dataframe: pd.core.frame.DataFrame, country: str) -> pd.core.frame.DataFrame:
    df_one_country = dataframe[dataframe['country'] == country]
    df_one_country = df_one_country.melt(
        var_name='year', value_name='population')
    df_one_country = df_one_country.drop((df_one_country.index[[0]]))
    df_one_country = df_one_country.head(-50)
    df_one_country['population'] = [float(value.rstrip('M'))
                                    for value in df_one_country['population']]
    return df_one_country


def main():
    try:
        df_population_total = load('population_total.csv')
    except Exception as error:
        print(f"An error occurred: {error}")
        exit(1)

    # filter out France's data
    df_country1 = get_country_data(df_population_total, 'France')
    df_country2 = get_country_data(df_population_total, 'Belgium')

    # plot a line graph
    # Set the x-axis tick positions and labels
    x_ticks = [str(year) for year in range(1800, 2050, 40)]
    x_tick_positions = list(range(1800, 2050, 40))
    y_ticks = [pop for pop in range(0, 80, 20)]

    # plot
    plt.plot(df_country1['year'], df_country1['population'],
             label='France', color='green')
    plt.plot(df_country2['year'], df_country2['population'],
             label='Belgium')

    plt.xticks(x_ticks, rotation='horizontal')

    plt.yticks(y_ticks)
   # Format the y-axis tick labels to include 'M'

    def millions(x, pos):
        return f'{int(x)}M'
    formatter = FuncFormatter(millions)
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend(loc='lower right')
    plt.show()


if __name__ == "__main__":
    main()
