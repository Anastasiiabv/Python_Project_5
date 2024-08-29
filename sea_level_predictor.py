import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
   # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(df['Year'].min(), 2075)
    sea_level_pred_1 = intercept + slope * years_extended
    plt.plot(years_extended, sea_level_pred_1, color='red')

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    years_extended_2 = np.arange(recent_data['Year'].min(), 2075)
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'],
                                                                                                recent_data[
                                                                                                    'CSIRO Adjusted Sea Level'])
    sea_level_pred_2 = intercept_recent + slope_recent * years_extended_2
    plt.plot(years_extended_2, sea_level_pred_2, color='green')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.grid(True)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
