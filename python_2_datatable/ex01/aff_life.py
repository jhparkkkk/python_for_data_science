import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def main():
    try:
        df_life_expectancy = load('life_expectancy_years.csv')
    except Exception as error:
        print(f"An error occurred: {error}")
        exit(1)

    # filter out France's data
    country = 'France'
    country_data = df_life_expectancy[df_life_expectancy['country'] == country]
    country_data = country_data.melt(
        var_name='year', value_name='life_expectancy')
    country_data = country_data.drop((country_data.index[[0]]))

    # plot a line graph
    # Set the x-axis tick positions and labels
    x_ticks = [str(year) for year in range(1800, 2101, 40)]
    x_tick_positions = list(range(1800, 2101, 40))
    # plot
    plt.plot(country_data['year'], country_data['life_expectancy'])
    plt.xticks(x_ticks, rotation='horizontal')
    # titles and labels
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')

    plt.show()


if __name__ == "__main__":
    main()
