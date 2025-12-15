import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent.resolve()
FIGURES_DIR = PROJECT_ROOT / "output" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

def save_and_show(fig_name:str) -> None:
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / fig_name, dpi = 300)
    plt.show()
    plt.close()

sns.set_theme(style='whitegrid')

#Horizontal bar plot for ranked data
def barh_plot(
        series: pd.Series,
        title: str,
        xlabel: str,
        ylabel: str = "Category",
        figsize=(12,7),
        file_name: str | None=None
) -> None:
        plt.figure(figsize=figsize)

        sns.barplot(x=series.values, y=series.index, palette='viridis',legend=False)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.tight_layout()

        for i,value in enumerate(series.values):
            plt.text(value,i, f"{value}", va='center')

        save_and_show(file_name)

#Bar chart ag distribution
def age_distribution_bar(df: pd.DataFrame) -> None:
    age_dist = df['Age'].value_counts().sort_index()

    plt.figure(figsize=(8,6))
    sns.barplot(
        y = age_dist.index,
        x = age_dist.values,
        palette='pastel'
    )
    plt.title("Age Distribution of Respondents")
    plt.xlabel('Number of respondents')
    plt.ylabel('Age')
    save_and_show('age_distribution_bar.png')


def barplot_salary_by_experience(df_result: pd.DataFrame) -> None:
    df_result.plot(kind='bar', figsize=(10,6))
    plt.title('Average and Median Salary by Experience Level')
    plt.ylabel('Salary (USD)')
    plt.xlabel('Experience Level')
    plt.xticks(rotation=0)
    save_and_show('barplot_salary_by_experience.png')

#Heatmap: Industry vs Python knowledge (median salary)
def industry_salary_heatmap(df: pd.DataFrame) -> None:
    heatmap_df = df.pivot_table(
        values='ConvertedCompYearly',
        index='Industry',
        columns='PythonKnowledge',
        aggfunc='median'
    )

    plt.figure(figsize=(10,8)),
    sns.heatmap(heatmap_df, cmap='coolwarm', annot=True, fmt='.0f')
    plt.title('Median Salary by Industry and Python Knowledge')
    save_and_show('industry_salary_heatmap.png')

def save_plotly(fig, file_name:str) -> None:
    fig.write_html(FIGURES_DIR / file_name)

#World map of respondents count
def respondents_world_map(df: pd.DataFrame) -> None:
    country_count = (
        df['Country']
        .value_counts()
        .rename_axis('Country')
        .reset_index(name='Respondents')
    )

    fig = px.choropleth(
        country_count,
        locations='Country',
        locationmode='country names',
        color='Respondents',
        hover_name='Country',
        color_continuous_scale='Sunset',
        title="Number of Respondents Across Countries"
    )

    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=True),
        template='plotly_white'
    )
    save_plotly(fig, 'respondents_world_map.html')







