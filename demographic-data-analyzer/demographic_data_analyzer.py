import pandas as pd
from pathlib import Path


def calculate_demographic_data(print_data=True):
    """
    Analyze demographic data from the 1994 Census dataset.

    The analysis includes:
    - Race distribution
    - Average age of men
    - Education levels
    - Income distribution
    - Working hours
    - Country income statistics
    - Most popular occupation in India among high earners

    Args:
        print_data (bool): Whether to display the results.

    Returns:
        dict: Dictionary containing all calculated demographic statistics.
    """

    # Locate dataset relative to this script
    base_path = Path(__file__).resolve().parent
    csv_path = base_path / "adult.data.csv"

    # Read dataset
    df = pd.read_csv(csv_path)

    # 1. Number of people of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df.loc[df["sex"] == "Male", "age"].mean(),
        1
    )

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100,
        1
    )

    # 4. Percentage of people with advanced education earning >50K
    higher_education = df["education"].isin([
        "Bachelors",
        "Masters",
        "Doctorate"
    ])

    higher_education_rich = round(
        (
            (higher_education & (df["salary"] == ">50K")).sum()
            / higher_education.sum()
        ) * 100,
        1
    )

    # 5. Percentage without advanced education earning >50K
    lower_education = ~higher_education

    lower_education_rich = round(
        (
            (lower_education & (df["salary"] == ">50K")).sum()
            / lower_education.sum()
        ) * 100,
        1
    )

    # 6. Minimum number of working hours per week
    min_work_hours = int(df["hours-per-week"].min())

    # 7. Percentage of minimum-hour workers earning >50K
    min_hour_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    rich_percentage = round(
        (
            min_hour_workers["salary"] == ">50K"
        ).mean() * 100,
        1
    )

    # 8. Country with the highest percentage of people earning >50K
    country_salary_stats = df.groupby("native-country")["salary"].apply(
        lambda salaries: (salaries == ">50K").mean() * 100
    )

    highest_earning_country = country_salary_stats.idxmax()

    highest_earning_country_percentage = round(
        country_salary_stats.max(),
        1
    )

    # 9. Most popular occupation among high earners in India
    india_high_earners = df[
        (df["native-country"] == "India")
        & (df["salary"] == ">50K")
    ]

    top_IN_occupation = (
        india_high_earners["occupation"]
        .value_counts()
        .idxmax()
    )

    # Display results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print(
            "Percentage with higher education that earn >50K:",
            higher_education_rich
        )
        print(
            "Percentage without higher education that earn >50K:",
            lower_education_rich
        )
        print("Min work time:", min_work_hours, "hours/week")
        print(
            "Percentage of rich among those who work fewest hours:",
            rich_percentage
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage
        )
        print(
            "Top occupations in India:",
            top_IN_occupation
        )

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }


if __name__ == "__main__":
    print("\nDEMOGRAPHIC DATA ANALYZER")
    print("=" * 60)

    calculate_demographic_data()