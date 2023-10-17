import matplotlib.pyplot as plt
from load_csv import load
from pandas.core.frame import DataFrame


def get_country_data(df: DataFrame, country: str) -> DataFrame:
    """from dataframe select row `country`
    Args:
        dataframe (pd.core.frame.DataFrame): dataframe to filter
        country (str): row name to select

    Raises:
        error: if dataframe filtering out is not ok

    Returns:
        pd.core.frame.DataFrame: selected dataframe
    """
    try:
        df_one_country = df[df['country'] == country]
        df_one_country = df_one_country.melt(
            var_name='year', value_name='life_expectancy')
        df_one_country = df_one_country.drop((df_one_country.index[[0]]))
        return df_one_country
    except Exception as error:
        raise error


def main():
    """loads the file
life_expectancy_years.csv, and displays the country information of my campus.
    """
    try:
        df_life_expectancy = load('life_expectancy_years.csv')
        df_one_country = get_country_data(df_life_expectancy, 'France')

    except Exception as error:
        print(f"An error occurred: {error}")
        exit(1)
    x_ticks = [str(year) for year in range(1800, 2101, 40)]
    # plot
    plt.plot(df_one_country['year'], df_one_country['life_expectancy'])
    plt.xticks(x_ticks, rotation='horizontal')
    # titles and labels
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')

    plt.show()


if __name__ == "__main__":
    main()
