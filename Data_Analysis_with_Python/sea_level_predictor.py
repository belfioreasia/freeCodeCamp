import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df['Year'],
               df['CSIRO Adjusted Sea Level'],
               label='collected data')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'],
                                           df['CSIRO Adjusted Sea Level'])
    years = range(1880, 2051)
    plt.plot(years, slope * years + intercept, 'r', label='line of best fit')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope, intercept, _, _, _ = linregress(df_2000['Year'],
                                           df_2000['CSIRO Adjusted Sea Level'])
    years = range(2000, 2051)
    plt.plot(years, slope * years + intercept, 'blue', label='prediction')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
