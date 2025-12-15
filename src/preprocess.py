import pandas as pd

LANGUAGES = ['Python', 'JavaScript', 'SQL', 'C#', 'R']
TOP_QUANTILE = 0.75

EXPERIENCE_BINS = [0,3,6,10,15,50]
EXPERIENCE_LABELS = ['Junior', 'Middle', 'Senior', 'Lead', 'Principal']

'''Clean and enrich survey data
    - handle missing values
    - normalize text fieldspy
    - bucket experience level'''

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df['RemoteWork'] = df['RemoteWork'].str.strip().str.lower()
    df['LanguageHaveWorkedWith'] = df['LanguageHaveWorkedWith'].fillna('')
    df['LearnCode'] = df['LearnCode'].fillna('')
    df['EdLevel'] = df['EdLevel'].fillna('Unknown')
    df['WorkExp'] = df['WorkExp'].fillna(df['WorkExp'].median())

    df['know_Python'] = df['LanguageHaveWorkedWith'].str.contains('Python', na=False)
    df['PythonKnowledge'] = df['know_Python'].map({
        True: 'Know Python',
        False: "Don't know Python"
    })
    df['learn_by_courses'] = df['LearnCode'].str.contains('Online Courses', na=False)

    for lang in LANGUAGES:
        df[f'know_{lang}'] = df['LanguageHaveWorkedWith'].str.contains(lang, na=False)

    df['ExperienceLevel'] = pd.cut(
        df['WorkExp'],
        bins=EXPERIENCE_BINS,
        labels=EXPERIENCE_LABELS
    )

    return df