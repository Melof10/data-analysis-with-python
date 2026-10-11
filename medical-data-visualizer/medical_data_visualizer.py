import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# ---------------------------------------------------------
# 1. Load medical examination dataset
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "medical_examination.csv")


# ---------------------------------------------------------
# 2. Calculate BMI and overweight indicator
# ---------------------------------------------------------

# BMI = weight (kg) / height (m)^2
bmi = df["weight"] / ((df["height"] / 100) ** 2)

# 0 = Not overweight
# 1 = Overweight (BMI > 25)
df["overweight"] = (bmi > 25).astype(int)


# ---------------------------------------------------------
# 3. Normalize cholesterol and glucose
# ---------------------------------------------------------

# 0 = Normal
# 1 = Above normal
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)


# ---------------------------------------------------------
# 4. Create categorical plot
# ---------------------------------------------------------

def draw_cat_plot():

    # Convert data into long format
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=[
            "cholesterol",
            "gluc",
            "smoke",
            "alco",
            "active",
            "overweight"
        ]
    )

    # Group by cardiovascular condition and indicators
    df_cat = (
        df_cat
        .groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # Create categorical plot
    cat_plot = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
        height=5,
        aspect=1.2
    )

    # Retrieve matplotlib figure
    fig = cat_plot.fig

    # Set labels required by freeCodeCamp tests
    cat_plot.set_axis_labels(
        "variable",
        "total"
    )

    # Customize panel titles
    cat_plot.set_titles(
        "Cardiovascular Disease: {col_name}"
    )

    # Rotate labels for readability
    for ax in cat_plot.axes.flat:
        ax.tick_params(axis="x", rotation=35)

    # Add figure title
    fig.suptitle(
        "Medical Examination: Categorical Feature Analysis",
        fontsize=14,
        fontweight="bold",
        y=1.05
    )

    fig.tight_layout()

    # Save figure
    fig.savefig(BASE_DIR / "catplot.png")

    return fig


# ---------------------------------------------------------
# 5. Create correlation heatmap
# ---------------------------------------------------------

def draw_heat_map():

    # Remove incorrect medical records
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (
            df["height"]
            >= df["height"].quantile(0.025)
        )
        & (
            df["height"]
            <= df["height"].quantile(0.975)
        )
        & (
            df["weight"]
            >= df["weight"].quantile(0.025)
        )
        & (
            df["weight"]
            <= df["weight"].quantile(0.975)
        )
    ].copy()

    # Calculate correlation matrix
    corr = df_heat.corr(numeric_only=True)

    # Create mask for upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        square=True,
        linewidths=0.5,
        center=0,
        cbar_kws={"shrink": 0.7},
        ax=ax
    )

    # Customize chart title
    ax.set_title(
        "Medical Examination: Correlation Heatmap",
        fontsize=14,
        fontweight="bold",
        pad=20
    )

    fig.tight_layout()

    # Save figure
    fig.savefig(BASE_DIR / "heatmap.png")

    return fig


# ---------------------------------------------------------
# 6. Main execution
# ---------------------------------------------------------

if __name__ == "__main__":

    print("\nMEDICAL DATA VISUALIZER")
    print("=" * 60)

    print("\nLoading medical examination dataset...")
    print(f"Total patients: {len(df):,}")

    print("\nGenerating categorical plot...")
    draw_cat_plot()
    print("Categorical plot generated: catplot.png")

    print("\nGenerating correlation heatmap...")
    draw_heat_map()
    print("Correlation heatmap generated: heatmap.png")

    print("\nAnalysis completed successfully.")
    