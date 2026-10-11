import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from pathlib import Path


def draw_plot():
    # Clear previous plots to prevent duplicated elements
    plt.clf()

    # Read data from file
    base_path = Path(__file__).resolve().parent
    csv_path = base_path / 'epa-sea-level.csv'

    df = pd.read_csv(csv_path)

    # Create scatter plot
    plt.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level'],
        color='#4682B4',
        alpha=0.7,
        s=25
    )

    # Create first line of best fit (1880–2050)
    regression_all = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    years_all = range(1880, 2051)

    sea_levels_all = [
        regression_all.slope * year + regression_all.intercept
        for year in years_all
    ]

    plt.plot(
        years_all,
        sea_levels_all,
        color='red',
        linewidth=2,
        label='Prediction from 1880'
    )

    # Create second line of best fit (2000–2050)
    df_recent = df[df['Year'] >= 2000]

    regression_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    years_recent = range(2000, 2051)

    sea_levels_recent = [
        regression_recent.slope * year + regression_recent.intercept
        for year in years_recent
    ]

    plt.plot(
        years_recent,
        sea_levels_recent,
        color='green',
        linewidth=2,
        label='Prediction from 2000'
    )

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Improve chart appearance
    plt.legend(loc='upper left')
    plt.grid(True, alpha=0.3)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


# Execute directly from VS Code or terminal
if __name__ == "__main__":
    print("Iniciando análisis del nivel del mar...")

    draw_plot()

    print("Análisis completado correctamente.")
    print("Gráfico generado: sea_level_plot.png")