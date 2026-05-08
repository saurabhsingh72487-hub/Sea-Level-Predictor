import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Predict sea levels through 2050
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_predicted = res.slope * years_extended + res.intercept

    # Plot first line
    ax.plot(years_extended, sea_levels_predicted, 'r')

    # Create second line of best fit using data from 2000 onward
    df_recent = df[df['Year'] >= 2000]

    res_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    # Predict sea levels through 2050
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = (
        res_recent.slope * years_recent + res_recent.intercept
    )

    # Plot second line
    ax.plot(years_recent, sea_levels_recent, 'green')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()