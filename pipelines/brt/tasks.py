from io import StringIO

import pandas as pd
from prefect import task
import requests

from utils import log

@task
def download_data() -> str:
    """
    Baixa dados da API https://dados.mobilidade.rio/gps/brt e retorna um texto em formato JSON.

    Returns:
        str: texto em formato JSON
    """
    response = requests.get(
        "https://dados.mobilidade.rio/gps/brt"
    )
    log("Dados baixados com sucesso!")
    return response.text

@task
def parse_data(data: str) -> pd.DataFrame:
    """
    Transforma os dados em formato JSON em um DataFrame do Pandas, para facilitar sua manipulação.

    Args:
        data (str): texto em formato JSON.

    Returns:
        pd.DataFrame: DataFrame do Pandas.
    """
    df = pd.read_json(StringIO(data))
    log("Dados convertidos em DataFrame com sucesso!")
    return df

@task
def save_report(dataframe: pd.DataFrame) -> None:
    """
    Salva o DataFrame em um arquivo CSV.

    Args:
        dataframe (pd.DataFrame): DataFrame do Pandas.
    """

    # Save dataframe to CSV + timestamp with full timestamp
    timestamp = pd.Timestamp.now().strftime("%Y%m%d%H%M%S")
    dataframe.to_csv(f"report_{timestamp}.csv", index=False)
    log("Dados salvos em report.csv com sucesso!")
