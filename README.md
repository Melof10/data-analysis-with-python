# Sea Level Predictor
### Data Analysis with Python | Professional Practice Project

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![SciPy](https://img.shields.io/badge/SciPy-Statistical%20Analysis-8CAAE6?logo=scipy)
![freeCodeCamp](https://img.shields.io/badge/freeCodeCamp-Data%20Analysis-0A0A23?logo=freecodecamp)
![Academic Project](https://img.shields.io/badge/Teclab-Professional%20Practice-green)

## 1. Project Overview

**Sea Level Predictor** is a Python-based data analysis project developed as part of the **Professional Practice coursework (Práctica Profesionalizante)** of the **Higher Technical Degree in Data Science at Teclab**.

The project is based on the **Sea Level Predictor challenge** from the **Data Analysis with Python certification by freeCodeCamp**.

Its main purpose is to analyze historical sea level measurements, identify long-term trends, and estimate future sea level changes through linear regression.

The project combines data processing, statistical analysis, predictive modeling, and data visualization to demonstrate the practical application of Python in a real-world environmental dataset.

### Academic Context

| Institution | Teclab |
|---|---|
| Academic Program | Higher Technical Degree in Data Science |
| Course | Professional Practice (Práctica Profesionalizante) |
| Project | Sea Level Predictor |
| Learning Platform | freeCodeCamp |
| Certification Track | Data Analysis with Python |
| Programming Language | Python |

---

## 2. Project Objectives

The primary objective is to analyze historical sea level data and generate predictions through 2050.

Specific objectives include:

- Importing and processing structured datasets using Pandas.
- Exploring historical sea level measurements.
- Visualizing historical observations through scatter plots.
- Applying linear regression to identify long-term trends.
- Comparing predictions generated from different historical periods.
- Estimating sea level changes through 2050.
- Producing reproducible data visualizations.
- Validating the implementation through automated unit tests.

---

## 3. Dataset

The project uses the `epa-sea-level.csv` dataset provided as part of the freeCodeCamp Sea Level Predictor exercise.

The dataset contains historical measurements of global mean sea level changes beginning in 1880.

### Main Variables

| Variable | Description |
|---|---|
| Year | Year of observation |
| CSIRO Adjusted Sea Level | Adjusted sea level measurement in inches |
| Lower Error Bound | Lower uncertainty estimate |
| Upper Error Bound | Upper uncertainty estimate |
| NOAA Adjusted Sea Level | Additional adjusted sea level measurements |

The analysis primarily uses the following variables:

- **Independent variable (X):** Year
- **Dependent variable (Y):** CSIRO Adjusted Sea Level

These variables are used to estimate the relationship between time and sea level changes.

---

## 4. Technologies and Libraries

The project was developed using Python and the following libraries.

### Python

The primary programming language used for data processing, statistical analysis, and visualization.

### Pandas

Used to import the CSV dataset, manipulate tabular data, and filter observations.

```python
import pandas as pd

df = pd.read_csv("epa-sea-level.csv")
```

### Matplotlib

Used to generate scatter plots, regression lines, and the final visualization.

```python
import matplotlib.pyplot as plt

plt.scatter(
    df["Year"],
    df["CSIRO Adjusted Sea Level"]
)
```

### SciPy

Used to calculate linear regression models through `scipy.stats.linregress`.

```python
from scipy.stats import linregress

regression = linregress(
    df["Year"],
    df["CSIRO Adjusted Sea Level"]
)
```

---

## 5. Methodology

The project follows a structured data analysis workflow.

### Step 1: Data Collection

Historical sea level measurements are imported from the CSV dataset.

### Step 2: Data Processing

Pandas is used to organize the dataset and select the variables required for statistical analysis.

### Step 3: Exploratory Data Visualization

A scatter plot is generated to visualize the relationship between observation year and sea level.

### Step 4: Historical Linear Regression

A linear regression model is calculated using the historical observations beginning in 1880.

The resulting regression line is extended through 2050.

### Step 5: Recent Linear Regression

A second regression model is calculated using observations from the year 2000 onward.

This model is also extended through 2050.

### Step 6: Comparative Analysis

Both regression lines are displayed alongside the historical measurements.

This comparison highlights how predictions may differ depending on the historical period selected for modeling.

---

## 6. Statistical Model

The project uses simple linear regression.

The model is represented by:

$begin:math:display$
\\hat\{y\} \= mx \+ b
$end:math:display$

Where:

- **x:** Observation year
- **ŷ:** Predicted sea level
- **m:** Regression slope
- **b:** Regression intercept

The regression parameters are calculated using SciPy:

```python
regression = linregress(
    df["Year"],
    df["CSIRO Adjusted Sea Level"]
)
```

Predictions are then generated using:

```python
predicted_levels = [
    regression.slope * year + regression.intercept
    for year in range(1880, 2051)
]
```

### Model Comparison

Two models are evaluated:

| Model | Training Period | Prediction Horizon |
|---|---|---|
| Historical Regression | 1880 onward | 2050 |
| Recent Regression | 2000 onward | 2050 |

The models provide different projections because they are fitted using different historical periods.

---

## 7. Data Visualization

The following chart was generated using Matplotlib.

### Global Sea Level Rise and Predictions Through 2050

![Sea Level Prediction](sea_level_plot.png)

### Chart Interpretation

The visualization includes three main components.

**Historical Observations (Blue Points)**

Represent the measured sea level changes over time.

**Historical Regression (Red Line)**

Represents the long-term linear trend calculated using observations beginning in 1880.

**Recent Regression (Green Line)**

Represents the trend calculated using observations from 2000 onward.

### Key Findings

The analysis indicates that:

1. Historical sea level measurements exhibit an increasing trend.
2. Both regression models predict continued sea level rise through 2050.
3. The regression model based on recent observations produces a steeper trend.
4. Predictions are sensitive to the historical period used for model estimation.

These findings illustrate the importance of selecting appropriate historical data when developing predictive models.

**Important:** These projections are statistical extrapolations and should not be interpreted as comprehensive climate model forecasts.

---

## 8. Project Structure

```text
sea-level-predictor/
│
├── sea_level_predictor.py
├── epa-sea-level.csv
├── sea_level_plot.png
├── test_module.py
├── README.md
└── .gitignore
```

### File Descriptions

| File | Description |
|---|---|
| `sea_level_predictor.py` | Main Python implementation |
| `epa-sea-level.csv` | Historical sea level dataset |
| `sea_level_plot.png` | Generated visualization |
| `test_module.py` | Automated tests provided by freeCodeCamp |
| `README.md` | Project documentation |
| `.gitignore` | Git exclusions for local and temporary files |

---

## 9. Installation and Setup

### Prerequisites

- Python 3.10 or newer
- pip
- Git
- A terminal or Python-compatible IDE

### Clone the Repository

```bash
git clone https://github.com/Melof10/sea-level-predictor.git
```

Navigate to the project directory:

```bash
cd sea-level-predictor
```

### Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the environment.

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
python -m pip install pandas matplotlib scipy
```

---

## 10. Running the Project

Execute the main Python script:

```bash
python sea_level_predictor.py
```

Expected console output:

```text
Iniciando análisis del nivel del mar...
Análisis completado correctamente.
Gráfico generado: sea_level_plot.png
```

The script generates the following file:

```text
sea_level_plot.png
```

This image contains the historical observations and both regression-based projections through 2050.

---

## 11. Automated Testing

The project includes automated unit tests provided by freeCodeCamp.

These tests verify that the implementation satisfies the requirements of the Sea Level Predictor challenge.

### Running the Tests

Execute:

```bash
python -m unittest test_module.py
```

### Successful Test Execution

The implementation was validated in GitHub Codespaces, where all four automated tests passed.

Example of a successful execution:

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.657s

OK
```

The execution time may vary depending on the environment.

### Validation Summary

| Validation | Result |
|---|---|
| Historical data visualization | Passed |
| Regression line using historical data | Passed |
| Regression line using data from 2000 onward | Passed |
| Chart labels and title | Passed |
| Automated tests | 4/4 Passed |

---

## 12. Learning Outcomes

Through this project, the following technical skills were practiced:

### Data Analysis

- Reading structured datasets.
- Selecting relevant variables.
- Filtering historical observations.
- Understanding relationships between numerical variables.

### Statistical Analysis

- Simple linear regression.
- Regression slope and intercept.
- Trend identification.
- Statistical extrapolation.

### Data Visualization

- Scatter plots.
- Regression line visualization.
- Axis labeling and chart formatting.
- Interpretation of historical trends.

### Software Development

- Python project organization.
- Dependency management.
- Virtual environments.
- Automated testing.
- Version control using Git and GitHub.

---

## 13. Academic and Professional Relevance

This project contributes to the development of practical skills required in the Data Science field.

As part of the **Professional Practice coursework at Teclab**, it provides an opportunity to apply theoretical concepts to a real dataset.

The implementation demonstrates a complete analytical workflow, from importing historical observations to producing and interpreting statistical predictions.

It also introduces fundamental concepts that support further study in:

- Predictive analytics.
- Machine learning.
- Time series analysis.
- Statistical modeling.
- Data-driven decision-making.

---

## 14. References

### freeCodeCamp

**Data Analysis with Python — Sea Level Predictor**

https://www.freecodecamp.org/learn/data-analysis-with-python/

Original project repository:

https://github.com/freeCodeCamp/boilerplate-sea-level-predictor

### Teclab

**Higher Technical Degree in Data Science**

https://www.teclab.edu.ar/

### Python Documentation

https://docs.python.org/3/

### Pandas Documentation

https://pandas.pydata.org/docs/

### Matplotlib Documentation

https://matplotlib.org/stable/

### SciPy Documentation

https://docs.scipy.org/doc/scipy/

---

## 15. Acknowledgments

This project was developed for educational purposes as part of the Professional Practice coursework in the Higher Technical Degree in Data Science at Teclab.

The original project requirements, dataset, and automated testing framework were provided by freeCodeCamp through its Data Analysis with Python curriculum.

The implementation was completed as an academic exercise to strengthen practical skills in Python programming, statistical analysis, and data visualization.

---

**Academic Program:** Higher Technical Degree in Data Science  
**Institution:** Teclab  
**Course:** Professional Practice (Práctica Profesionalizante)  
**Project:** Sea Level Predictor  
**Learning Platform:** freeCodeCamp  
**Language:** Python