import prefect
from dotenv import load_dotenv
import os
import psycopg2

def log(message) -> None:
    """Logs a message"""
    prefect.context.logger.info(f"\n{message}")

def create_environment() -> None:
    """
    Creates schema and table in Postgres
    """

    load_dotenv()

    host = os.getenv("HOST")
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    port = os.getenv("PORT")
    database = os.getenv("DATABASE")
        
    # Connect to Postgres
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        port=port,
        database=database
    )

    # Create cursor
    cursor = conn.cursor()

    # Create schema if it does not exist
    cursor.execute("CREATE SCHEMA IF NOT EXISTS transporte_rodoviario_gps;")

    log("Schema criado com sucesso!")

    # Set datestyle to ISO, MDY to avoid datestyle conflicts
    cursor.execute("SET datestyle TO 'ISO, MDY';")

    # Create table in Postgres if not exists
    cursor.execute("""CREATE TABLE IF NOT EXISTS transporte_rodoviario_gps.dados_brt (
                        id SERIAL PRIMARY KEY,
                        codigo VARCHAR(255),
                        placa VARCHAR(255),
                        linha VARCHAR(255),
                        latitude FLOAT,
                        longitude FLOAT,
                        datahora TIMESTAMP WITH TIME ZONE,
                        velocidade FLOAT,
                        id_migracao_trajeto VARCHAR(255),
                        sentido VARCHAR(255),
                        trajeto VARCHAR(255),
                        hodometro VARCHAR(255),
                        direcao VARCHAR(255)
                );""")
    
    # Commit changes
    conn.commit()

    # Close cursor and connection
    cursor.close()
    conn.close()

    log("Tabela criada com sucesso!")