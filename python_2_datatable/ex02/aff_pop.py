from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker


def get_country_data(dataframe: pd.core.frame.DataFrame,
                     country: str) -> pd.core.frame.DataFrame:
    """from dataframe select row `country` and select columns '1850' to '2050'
    Args:
        dataframe (pd.core.frame.DataFrame): dataframe to filter
        country (str): row name to select

    Raises:
        error: if dataframe filtering out is not ok

    Returns:
        pd.core.frame.DataFrame: selected dataframe
    """
    try:
        df_one_country = dataframe[dataframe['country'] == country]
        df_one_country = df_one_country.melt(
            var_name='year', value_name='population')
        df_one_country = df_one_country.drop((df_one_country.index[[0]]))
        df_one_country = df_one_country.head(-50)
        df_one_country['population'] = [float(value.rstrip('M'))
                                        for value in df_one_country['population']]
        return df_one_country
    except Exception as error:
        raise error


def millions(x, pos):
    """convert 1000000 to `1M`

    Args:
        x (int): value
        pos (None): position
    Returns:
        str: converted value
    """
    return f'{int(x)}M'


def main():
    """loads the file
population_total.csv, and displays the country information
of your campus versus other country of your choice.
    """
    try:
        df_population_total = load('population_total.csv')
        # filter out France's and Belgium's data
        df_country1 = get_country_data(df_population_total, 'France')
        df_country2 = get_country_data(df_population_total, 'Belgium')
    except Exception as error:
        print(f"An error occurred: {error}")
        exit(1)

    # plot a line graph
    # Set the x-axis tick positions and labels
    x_ticks = [str(year) for year in range(1800, 2050, 40)]
    y_ticks = [pop for pop in range(0, 80, 20)]

    # plot
    plt.plot(df_country2['year'], df_country2['population'],
             label='Belgium')
    plt.plot(df_country1['year'], df_country1['population'],
             label='France', color='green')

    plt.xticks(x_ticks, rotation='horizontal')

    plt.yticks(y_ticks)

    # Format the y-axis tick labels to include 'M'

    formatter = ticker.FuncFormatter(millions)
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend(loc='lower right')
    plt.show()


if __name__ == "__main__":
    main()
