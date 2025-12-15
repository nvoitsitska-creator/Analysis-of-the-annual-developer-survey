import pandas as pd
import zipfile
from typing import Tuple

def load_data_from_zip(zip_path: str) -> Tuple[pd.DataFrame,pd.DataFrame]:
    with zipfile.ZipFile(zip_path, 'r') as z:
        public = pd.read_csv(z.open('survey_results_public.csv'))
        schema = pd.read_csv(z.open('survey_results_schema.csv'))
    return public, schema