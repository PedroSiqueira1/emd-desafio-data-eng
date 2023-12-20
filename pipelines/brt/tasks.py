import pandas as pd
from prefect import task
import requests
from utils import log
from dotenv import load_dotenv
import os
import json
from sqlalchemy import create_engine
from datetime import datetime


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
    Transforma os dados em formato JSON para um DataFrame do Pandas, para facilitar sua manipulação.

    Args:
        data (str): texto em formato JSON.

    Returns:
        pd.DataFrame: DataFrame do Pandas.
    """
    data = json.loads(data)
    df = pd.json_normalize(data['veiculos'])

    log("Dados convertidos em DataFrame com sucesso!")

    return df

@task
def transform_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma os dados do DataFrame para uma forma mais adequada para o banco de dados.

    Args:
        dataframe (pd.DataFrame): DataFrame do Pandas.

    Returns:
        pd.DataFrame: DataFrame do Pandas.
    """ 

    # Rename DataHora Column
    dataframe.rename(columns={"dataHora": "datahora"}, inplace=True)

    # Convert datahora column to ISO-8601 format
    dataframe["datahora"] = dataframe["datahora"].apply(lambda x: datetime.utcfromtimestamp(x / 1000).isoformat())

    log("Dados transformados com sucesso!")

    return dataframe
@task
def save_report(dataframe: pd.DataFrame) -> None:
    """
    Salva o DataFrame em um arquivo CSV.

    Args:
        dataframe (pd.DataFrame): DataFrame do Pandas.
    """

    if not os.path.exists("report.csv"):
        dataframe.to_csv("report.csv", index=False, mode="w")
    else:
        dataframe.to_csv("report.csv", index=False, mode="a", header=False)

    log("Dados salvos em report.csv com sucesso!")



@task
def load_to_postgres(dataframe: pd.DataFrame) -> None:
    """
    Salva o DataFrame em um banco de dados Postgres.

    Args:
        dataframe (pd.DataFrame): DataFrame do Pandas.
    """

    # Connect to Postgres using SQLAlchemy
    
    load_dotenv()
    host = os.getenv("HOST")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    port = os.getenv("PORT")
    database = os.getenv("DATABASE")
    dialect = os.getenv("DIALECT")

    engine = create_engine(f'{dialect}://{user}:{password}@{host}:{port}/{database}', echo=True)

    # Load dataframe to Postgres
    dataframe.to_sql("dados_brt", engine, schema="transporte_rodoviario_gps", if_exists='append', index=False)

    # Close SQLAlchemy connection
    engine.dispose()

    log("Dados salvos no Postgres com sucesso!")
