import pandas as pd
import logging
from pathlib import Path
from src.config.settings import DATA_DIR
from typing import Optional

def load_data(filename: str = "challenge.xlsx") -> pd.DataFrame:
    try:
        file_path = DATA_DIR / filename
        df = pd.read_excel(file_path)
        df.columns = df.columns.str.strip()
        return df
    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Erro ao ler o arquivo {file_path}: {e}")
        raise