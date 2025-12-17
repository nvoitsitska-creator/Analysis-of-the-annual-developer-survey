# Analysis-of-the-Annual-Developer-Survey

## Project Overview

This project presents an end-to-end data analysis of the **Stack Overflow Developer Survey** dataset.  
The analysis focuses on understanding how **experience, programming skills, remote work, and industry**
affect developers’ compensation and demographics.

The project demonstrates practical skills in **data cleaning, exploratory data analysis, statistical aggregation,
and data visualization** using Python.

## Objectives

- Clean and preprocess raw survey data
- Engineer analytical features (experience levels, skill flags)
- Analyze salary trends across experience levels and skills
- Compare compensation for Python vs non-Python developers
- Explore the impact of remote work on salary
- Identify industries with the highest number of high-paid remote professionals
- Communicate insights using clear visualizations

## Analytical Questions

- How does salary change with experience level?
- Does Python knowledge impact median salary?
- Which programming languages are associated with higher pay?
- Are remote developers paid more than on-site employees?
- Which industries employ the most high-paid remote developers?
- How is the global developer population distributed?

## 📁 Project Structure
```
Annual_Developer_Survey/
│
├── data/ # Original survey datasets
│ └── stack-overflow-developer-survey-2025.zip
│   ├── survey_results_public.csv
│   └── survey_results_schema.csv
│
├── notebooks/ # Jupyter notebooks
│ └── analysis_notebook.ipynb # Main exploratory analysis
│
├── src/ # Source code
│ ├── load.py # Functions to load datasets
│ ├── preprocess.py # Data cleaning and feature engineering
│ ├── analysis.py # Statistical and analytical functions
│ └── visualization.py # Plots, charts, and maps
│
├── output/ # Generated output
│ ├── tables/ # CSV tables with computed metrics
│ └── figures/ # Charts, barplots, heatmaps
│
├── README.md
└── requirements.txt
└── respondents_world_map.html
```
## Tools & Technologies

- **Python**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **Plotly (interactive maps)**
- **Jupyter Notebook**

## Data Preparation
Key preprocessing steps:
- Handling missing values
- Normalizing text fields
- Creating binary skill indicators ('know_Python', 'know_SQL', etc.)
- Categorizing work experience into levels:
  - Junior
  - Middle
  - Senior
  - Lead
  - Principal

## Installation

1. Clone the repository:
```
git clone <https://github.com/nvoitsitska-creator/Analysis-of-the-annual-developer-survey.git>
cd Annual_Developer_Survey
```

3. Create and activate a virtual environment:
```python -m venv .venv```

  - **Windows**
```.venv\Scripts\activate```

  - **macOS/Linux**
```source .venv/bin/activate```

3. Install dependencies:
```pip install -r requirements.txt```

4. Load and preprocess data
```
from src.load import load_data_from_zip
from src.preprocess import preprocess_data

survey_df, schema_df = load_data_from_zip(
    '../data/stack-overflow-developer-survey-2025.zip'
)
df = preprocess_data(survey_df)
```

## 📈Analysis & Visualizations
### Experience & Salary
- Mean and median salaries increase consistently with experience
- Average salary grows faster than median, indicating high-end outliers
![Salary by Experience Level](https://github.com/nvoitsitska-creator/Analysis-of-the-annual-developer-survey/blob/master/output/figures/barplot_salary_by_experience.png?raw=true)

### Programming Languages
- R and C# have the highest median salaries
- Python is widely used and provides a moderate salary advantage
- JavaScript shows slightly lower median compensation
![Salary by Programming Language](https://github.com/nvoitsitska-creator/Analysis-of-the-annual-developer-survey/blob/master/output/figures/salary_by_language.png?raw=true)

### Python Impact
- Python developers earn more in most industries
- The strongest effect is observed in FinTech and Healthcare
![Industry Salary Heatmap](https://github.com/nvoitsitska-creator/Analysis-of-the-annual-developer-survey/blob/master/output/figures/industry_salary_heatmap.png?raw=true)

### Remote Work
- Fully remote roles show higher median salaries
- On-site roles have the lowest compensation

### Industry Insights
- Software Development dominates high-paid remote positions
- FinTech and Healthcare also show strong representation
![Industries among High-Paid Remote Workers](https://github.com/nvoitsitska-creator/Analysis-of-the-annual-developer-survey/blob/master/output/figures/Industries_among_High-paid_Remote_Workers.png?raw=true)

### Age Distribution
- Visualizes how respondents are distributed by age
![Age Distribution](https://github.com/nvoitsitska-creator/Analysis-of-the-annual-developer-survey/blob/master/output/figures/age_distribution_bar.png?raw=true)

### Global Distribution
- Respondents are concentrated in North America, Europe, and India
- Participation reflects global IT market development
  
**🌍Interactive Map**
  
Explore the global developer distribution on this interactive map: 
[View World Map](https://nvoitsitska-creator.github.io/Analysis-of-the-annual-developer-survey/respondents_world_map.html)

## 📊Looker Studio Dashboard

Explore the interactive dashboard on Looker Studio:

[View Dashboard](https://lookerstudio.google.com/reporting/12cf5bbe-9486-44d5-bf83-08c40de09a6f)


## Output Artifacts
### CSV tables with calculated metrics:
- Salary by experience level
- Salary by programming language
- Python vs non-Python salary
- Remote work salary comparison

### Visualizations:
- Bar charts
- Horizontal rankings
- Heatmaps
- Interactive world map (HTML)

## Key Insights
- Experience level strongly correlates with compensation
- Remote work is associated with higher salaries
- Python knowledge provides a measurable salary advantage
- Software-focused industries dominate high-paid remote work

## Author
**Anastasiia Voitsitska**

***Data Analyst***

📌 This project is part of my data analytics portfolio and demonstrates practical skills in data analysis,
data visualization, and insight communication.

