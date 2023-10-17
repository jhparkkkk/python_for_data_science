import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load
import numpy as np
def main():
    try:
        life_expectancy = load('life_expectancy_years.csv')
    except Exception as error:
        print(f"An error occurred: {error}")
        exit(1)
    column_names = life_expectancy.columns
    print(column_names)
    country = 'France'
 
    country_data = life_expectancy[life_expectancy['country'] == country]
    years = [str(year) for year in range(1800, 2101)]
    country_data = country_data[years]

    country_data = country_data.melt(var_name='year', value_name='life_expectancy')
    print(country_data)
    plt.plot(country_data[life_expectancy], country_data[years])
    plt.xlabel('Year', labelpad=100)
    plt.ylabel('Life Expectancy')
    plt.title(f'{country} Life expectancy Projections')
    years_to_display = ['1800', '1840']
    x = [1, 2] 
    plt.xticks(x, years_to_display)
    plt.show()

if __name__ == "__main__":
    main()
