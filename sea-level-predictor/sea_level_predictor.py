import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    fig, ax = plt.subplots()
    ax.scatter(x= "Year", y = "CSIRO Adjusted Sea Level", data = df)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years = pd.Series(range(1880,2050))
    ax.plot(years, intercept + slope*years, 'r', label='first line of best fit')
    df2 = df.loc[df["Year"] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    years2 = pd.Series(range(2000,2050))
    ax.plot(years2, intercept2 + slope2*years2, 'b', label='second line of best fit')
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")
    plt.savefig('sea_level_plot.png')
    return plt.gca()