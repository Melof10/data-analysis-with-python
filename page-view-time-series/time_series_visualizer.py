import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# ---------------------------------------------------------
# 1. Load dataset
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(
    BASE_DIR / "fcc-forum-pageviews.csv",
    parse_dates=["date"],
    index_col="date"
)


# ---------------------------------------------------------
# 2. Clean dataset
# ---------------------------------------------------------

df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
].copy()


# ---------------------------------------------------------
# 3. Line plot
# ---------------------------------------------------------

def draw_line_plot():

    df_line = df.copy()

    fig, ax = plt.subplots(figsize=(15, 6))

    ax.plot(
        df_line.index,
        df_line["value"],
        color="red",
        linewidth=1
    )

    ax.set_title(
        "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    ax.grid(True, alpha=0.25)

    fig.tight_layout()

    fig.savefig(BASE_DIR / "line_plot.png")

    return fig


# ---------------------------------------------------------
# 4. Bar plot
# ---------------------------------------------------------

def draw_bar_plot():

    df_bar = df.copy()

    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month

    monthly_average = (
        df_bar
        .groupby(["year", "month"])["value"]
        .mean()
        .unstack()
    )

    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    monthly_average = monthly_average.reindex(
        columns=range(1, 13)
    )

    monthly_average.columns = month_names

    fig, ax = plt.subplots(figsize=(12, 8))

    monthly_average.plot(
        kind="bar",
        ax=ax,
        width=0.8
    )

    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")

    ax.legend(
        title="Months",
        loc="upper left"
    )

    ax.tick_params(axis="x", rotation=0)

    ax.grid(axis="y", alpha=0.2)

    fig.tight_layout()

    fig.savefig(BASE_DIR / "bar_plot.png")

    return fig


# ---------------------------------------------------------
# 5. Box plots
# ---------------------------------------------------------

def draw_box_plot():

    df_box = df.copy()

    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.month

    month_names = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec"
    ]

    df_box["month"] = pd.Categorical(
        df_box["month"].map(
            dict(enumerate(month_names, start=1))
        ),
        categories=month_names,
        ordered=True
    )

    fig, axes = plt.subplots(
        nrows=1,
        ncols=2,
        figsize=(16, 6)
    )

    sns.boxplot(
        data=df_box,
        x="year",
        y="value",
        ax=axes[0]
    )

    axes[0].set_title(
        "Year-wise Box Plot (Trend)"
    )

    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(
        data=df_box,
        x="month",
        y="value",
        order=month_names,
        ax=axes[1]
    )

    axes[1].set_title(
        "Month-wise Box Plot (Seasonality)"
    )

    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.tight_layout()

    fig.savefig(BASE_DIR / "box_plot.png")

    return fig


# ---------------------------------------------------------
# 6. Main execution
# ---------------------------------------------------------

if __name__ == "__main__":

    print("\nPAGE VIEW TIME SERIES VISUALIZER")
    print("=" * 60)

    print("\nLoading freeCodeCamp forum dataset...")
    print(f"Total records after cleaning: {len(df):,}")

    print("\nGenerating line plot...")
    draw_line_plot()
    print("Line plot generated: line_plot.png")

    print("\nGenerating bar plot...")
    draw_bar_plot()
    print("Bar plot generated: bar_plot.png")

    print("\nGenerating box plots...")
    draw_box_plot()
    print("Box plots generated: box_plot.png")

    print("\nAnalysis completed successfully.")