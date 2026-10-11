# Data Analysis with Python

### Professional Practice | Data Science | Teclab

This repository contains five data analysis projects developed as part of the **Professional Practice course of the Higher Technical Degree in Data Science at Teclab**.

The projects are based on the **Data Analysis with Python certification program by freeCodeCamp**, combining theoretical knowledge with practical applications of statistical analysis, data processing, and visualization.

Each project addresses a different analytical problem using Python and its main data science libraries.

---

## Technologies & Tools

| Technology | Purpose |
|------------|---------|
| Python | Data processing and analysis |
| NumPy | Numerical and statistical calculations |
| Pandas | Data manipulation and transformation |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| SciPy | Statistical modeling and linear regression |
| Git & GitHub | Version control and project management |

---

## Projects

### 1. Mean-Variance-Standard Deviation Calculator

**Objective:** Apply fundamental statistical operations to a numerical dataset.

This project uses NumPy to transform a list of nine numbers into a 3×3 matrix and calculate descriptive statistics across rows, columns, and the entire matrix.

**Key concepts:**
- Multidimensional arrays
- Mean, variance, and standard deviation
- Minimum, maximum, and sum
- Matrix operations and data validation

**Result:**

![Mean Variance Calculator](mean-variance-calculator/mean_var_std.png)

---

### 2. Demographic Data Analyzer

**Objective:** Explore demographic characteristics and identify patterns related to education, occupation, and income.

Using a dataset derived from the U.S. Census, this project applies Pandas to analyze demographic distributions and relationships between socioeconomic variables.

**Key concepts:**
- Exploratory Data Analysis (EDA)
- Data filtering and aggregation
- Demographic and income analysis
- Statistical comparisons between population groups

**Result:**

![Demographic Data Analysis](demographic-data-analyzer/demographic_data_analyzer.png)

---

### 3. Medical Data Visualizer

**Objective:** Analyze medical examination records to explore relationships between cardiovascular conditions and health indicators.

The project includes data preprocessing, BMI calculations, normalization of medical indicators, and correlation analysis.

**Key concepts:**
- Data cleaning and preprocessing
- Body Mass Index (BMI)
- Categorical data visualization
- Correlation matrices and heatmaps

**Categorical Plot**

![Medical Categorical Plot](medical-data-visualizer/catplot.png)

**Correlation Heatmap**

![Medical Correlation Heatmap](medical-data-visualizer/heatmap.png)

---

### 4. Page View Time Series Visualizer

**Objective:** Analyze website traffic trends and seasonal patterns using historical time series data.

This project examines daily page views from the freeCodeCamp forum between May 2016 and December 2019.

The analysis includes outlier removal, monthly averages, and comparisons of page view distributions across different periods.

**Key concepts:**
- Time series analysis
- Outlier detection using percentiles
- Monthly and yearly aggregations
- Trend and seasonality analysis

**Daily Page Views**

![Page Views Line Plot](page-view-time-series/line_plot.png)

**Monthly Average Page Views**

![Page Views Bar Plot](page-view-time-series/bar_plot.png)

**Yearly and Monthly Distributions**

![Page Views Box Plot](page-view-time-series/box_plot.png)

---

### 5. Sea Level Predictor

**Objective:** Analyze historical sea level measurements and estimate future changes using statistical modeling.

The project applies linear regression to historical sea level data, comparing long-term trends with more recent observations to project sea level changes through 2050.

**Key concepts:**
- Linear regression
- Historical data analysis
- Trend estimation
- Predictive modeling and visualization

**Result:**

![Sea Level Prediction](sea-level-predictor/sea_level_plot.png)

---

## Project Structure

```text
data-analysis-with-python/
│
├── mean-variance-calculator/
├── demographic-data-analyzer/
├── medical-data-visualizer/
├── page-view-time-series/
├── sea-level-predictor/
│
├── .gitignore
└── README.md
```

Each project directory contains its Python implementation, the corresponding dataset when required, unit tests, and generated visualizations.

---

## Learning Outcomes

Through these projects, the following technical competencies were applied and reinforced:

- Data manipulation and transformation using Python.
- Exploratory and descriptive statistical analysis.
- Data cleaning and outlier detection.
- Numerical operations with multidimensional arrays.
- Data visualization and interpretation.
- Time series analysis and predictive modeling.
- Code validation through automated unit testing.

These competencies represent fundamental skills for working with real-world datasets and developing data-driven solutions.

---

## Academic Context

| | |
|---|---|
| **Institution** | Teclab |
| **Degree** | Higher Technical Degree in Data Science |
| **Course** | Professional Practice |
| **Learning Platform** | freeCodeCamp |
| **Certification Program** | Data Analysis with Python |
| **Projects Completed** | 5 |

The projects were developed for academic and educational purposes, applying the concepts covered in the freeCodeCamp curriculum within the framework of Teclab's Professional Practice course.

---

## References

- [freeCodeCamp — Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/)
- [Teclab — Official Website](https://www.teclab.edu.ar/)