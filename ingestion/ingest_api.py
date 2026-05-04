import requests
import pandas as pd
from datetime import datetime
import logging

# =========================
# CONFIG
# =========================

URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
OUTPUT_FILE = "data/selic_raw.csv"

# =========================
# LOGGING
# =========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =========================
# EXTRACT
# =========================

def extract():
    logging.info("Iniciando extração da API do Banco Central")

    response = requests.get(URL)
    response.raise_for_status()

    data = response.json()

    logging.info(f"{len(data)} registros extraídos")
    return data

# =========================
# TRANSFORM
# =========================

def transform(data):
    logging.info("Iniciando transformação dos dados")

    df = pd.DataFrame(data)

    # renomear para padrão RAW
    df.rename(columns={
        'data': 'data_raw',
        'valor': 'valor_raw'
    }, inplace=True)

    # limpeza básica
    df = df.dropna()

    # adicionar metadata
    df['data_carga'] = datetime.now()

    logging.info("Transformação concluída")
    return df

# =========================
# LOAD
# =========================

def load(df):
    logging.info("Salvando dados na camada RAW (CSV)")

    df.to_csv(OUTPUT_FILE, index=False)

    logging.info(f"Arquivo salvo em: {OUTPUT_FILE}")

# =========================
# PIPELINE
# =========================

def run_pipeline():
    data = extract()
    df = transform(data)
    load(df)

    logging.info("Pipeline finalizado com sucesso")

# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    run_pipeline()
