import pandas as pd

# Example loading from Gapminder
url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
gapminder = pd.read_csv(url)
gapminder.head()

# 1. Filter data for year 2007
# 2. Find the minimum life expectancy
# 3. Identify which country has this value

data_2007 = gapminder[gapminder['year'] == 2007]
min_life_exp = data_2007['lifeExp'].min()
country_min_life_exp = data_2007[data_2007['lifeExp'] == min_life_exp]['country'].values[0]
print(f"Country with minimum life expectancy in 2007: {country_min_life_exp} with life expectancy of {min_life_exp}")

# Use value_counts() or groupby to count countries per continent
# (Use the most recent year to avoid counting countries multiple times)
latest_year = gapminder['year'].max()
data_latest = gapminder[gapminder['year'] == latest_year]
countries_per_continent = data_latest['continent'].value_counts()
print("Number of countries per continent in the latest year:")
print(countries_per_continent)

# 1. Filter for 2007
# 2. Group by continent
# 3. Calculate mean GDP per capita
# 4. Find the maximum
gdp_per_continent = data_2007.groupby('continent')['gdpPercap'].mean()
max_gdp_continent = gdp_per_continent.idxmax()
max_gdp_value = gdp_per_continent.max()
print(f"Continent with highest average GDP per capita in 2007: {max_gdp_continent} with GDP per capita of {max_gdp_value}")

# 1. Get data for 1952 and 2007
# 2. Calculate the difference
# 3. Find the maximum
data_1952 = gapminder[gapminder['year'] == 1952]
gdp_diff = data_2007.set_index('country')['gdpPercap'] - data_1952.set_index('country')['gdpPercap']
max_gdp_increase_country = gdp_diff.idxmax()
max_gdp_increase_value = gdp_diff.max()
print(f"Country with highest increase in GDP per capita from 1952 to 2007: {max_gdp_increase_country} with an increase of {max_gdp_increase_value}")

# Find countries in Asia with population > 100 million and life expectancy > 70 in 2007
asian_countries = data_2007[(data_2007['continent'] == 'Asia') & 
                             (data_2007['pop'] > 100_000_000) & 
                             (data_2007['lifeExp'] > 70)]
print("Asian countries with population > 100 million and life expectancy > 70 in 2007:")
print(asian_countries[['country', 'pop', 'lifeExp']])

# Create a complete analysis report
report = {
    "min_life_expectancy": {
        "country": country_min_life_exp,
        "life_expectancy": min_life_exp
    },
    "countries_per_continent": countries_per_continent.to_dict(),
    "max_gdp_per_capita": {
        "continent": max_gdp_continent,
        "gdp_per_capita": max_gdp_value
    },
    "max_gdp_increase": {
        "country": max_gdp_increase_country,
        "gdp_increase": max_gdp_increase_value
    },
    "asian_countries_population_life_expectancy": asian_countries[['country', 'pop', 'lifeExp']].to_dict(orient='records')
}
print("Analysis Report:")
print(report)