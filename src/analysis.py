import pandas as pd
from typing import Set
from pathlib import Path

from src.preprocess import LANGUAGES

PROJECT_ROOT = Path(__file__).parent.parent.resolve()  # якщо файл у src/ або notebooks/
TABLES_DIR = PROJECT_ROOT / "output" / "tables"
TABLES_DIR.mkdir(parents=True, exist_ok=True)

#Function to save all tables
def save_table(
        df: pd.DataFrame,
        file_name: str
) -> None:
    df.to_csv(TABLES_DIR / file_name, index=True, encoding='utf-8')

#Count the number of respondents who answered all questions
def respondents_with_all_answers(
        survey_df: pd.DataFrame,
        schema_df: pd.DataFrame
) -> int:
    questions: Set[str] = set(schema_df['qname'].dropna())
    common_questions = list(questions.intersection(survey_df.columns))
    complete_responses = survey_df.dropna(subset=common_questions)
    return complete_responses.shape[0]

#Compute descriptive statistics for work experience
def workexp_stats(df: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame({
        "Metric": ['Mean', "Median", "Mode"],
        "WorkExp": [
            round(df['WorkExp'].mean(),2),
            df['WorkExp'].median(),
            df['WorkExp'].mode().iloc[0]]
                          }).set_index('Metric')

    save_table(result, 'work_experience_stats.csv')
    return result

#Count mean and median salary by experience level
def salary_by_experience_level(df: pd.DataFrame) -> pd.DataFrame:
    salary_df = df[df['ConvertedCompYearly'].notna()]

    result = (salary_df.groupby('ExperienceLevel',observed=True)['ConvertedCompYearly']
        .agg(['mean','median'])
        .round(0)
        .rename(columns={'mean':'Average salary','median':'Median salary'})
    )
    save_table(result, 'salary_by_experience_level.csv')
    return result

#Compare median salary for Python vs non-Python developers
def python_vs_non_python_salary(df: pd.DataFrame) -> pd.DataFrame:
    salary_df = df[df['ConvertedCompYearly'].notna()]

    result = (salary_df.groupby('know_Python')['ConvertedCompYearly']
              .median()
              .to_frame(name='Median Salary')
              )
    save_table(result, 'python_vs_non_python_salary.csv')
    return result

#Count median salary by remote work type
def remote_work_salary(df: pd.DataFrame) -> pd.DataFrame:
    salary_df = df[df['ConvertedCompYearly'].notna()]
    result = (salary_df.groupby('RemoteWork')['ConvertedCompYearly']
              .median()
              .to_frame(name='MedianSalary')
              .sort_values('MedianSalary', ascending=False)
              )
    save_table(result, 'remote_work_salary.csv')
    return result

#Count median salary by most popular languages
def salary_by_language(df: pd.DataFrame) -> pd.DataFrame:
    salary_df = df[df['ConvertedCompYearly'].notna()]

    data = {
        lang: salary_df.loc[salary_df[f'know_{lang}'], 'ConvertedCompYearly'].median()
        for lang in LANGUAGES
    }
    result = (
        pd.DataFrame.from_dict(data, orient='index',columns=['MedianSalary'])
        .sort_values('MedianSalary',ascending=False)
    )
    save_table(result, 'salary_by_language.csv')
    return result

#Count high-paid remote workers by industry
def high_paid_remote_by_industry(
        df: pd.DataFrame,
        top_quantile: float,
) -> pd.Series:
    threshold = df['ConvertedCompYearly'].quantile(top_quantile)

    filtered = df[
        (df['ConvertedCompYearly'] >= threshold)
        & (df['RemoteWork'].str.contains('remote', na=False))
    ]
    industry_count = (filtered.groupby('Industry')['ResponseId']
                 .nunique()
                 .sort_values(ascending=False)
                 .head()
                 )

    return industry_count

