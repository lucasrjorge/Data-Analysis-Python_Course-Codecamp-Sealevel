import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # 3. Create first line of best fit (for all data)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Extend the years to 2050 for the prediction
    years_extended = pd.Series(range(1880, 2051))
    sea_level_predicted = intercept + slope * years_extended

    # Plot first line of best fit
    plt.plot(years_extended, sea_level_predicted, color='blue', label='Best Fit (1880-2019)')

    # 4. Create second line of best fit (for data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Predict sea level using data from 2000 onwards
    sea_level_predicted_recent = intercept_recent + slope_recent * years_extended

    # Plot second line of best fit
    plt.plot(years_extended, sea_level_predicted_recent, color='green', label='Best Fit (2000-2019)')

    # 5. Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # 6. Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Testando a função para verificar o funcionamento
draw_plot()
