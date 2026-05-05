import requests
import os
import oracledb
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

tickers = ["PETR4", "VALE3", "ITUB4", "BBDC4"]

API_KEY = os.getenv("SERPAPI_KEY")

conn = oracledb.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    dsn=os.getenv("DB_DSN")
)

cursor = conn.cursor()

for ticker in tickers:

    params = {
        "q": f"{ticker} ações brasil",
        "hl": "pt",
        "gl": "br",
        "api_key": API_KEY
    }

    response = requests.get("https://serpapi.com/search.json", params=params)
    data = response.json()

    for result in data.get("organic_results", []):
        cursor.execute("""
            INSERT INTO RAW_NEWS_STOCKS 
            (ticker, titulo, snippet, data_carga)
            VALUES (:1, :2, :3, :4)
        """, [
            ticker,
            result.get("title"),
            result.get("snippet"),
            datetime.now()
        ])

conn.commit()
cursor.close()
conn.close()
