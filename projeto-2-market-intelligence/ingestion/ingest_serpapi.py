import os
import requests
import oracledb
from datetime import datetime

# =========================
# CONFIG (via env)
# =========================

API_KEY = os.getenv("SERPAPI_KEY")

DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "dsn": os.getenv("DB_DSN")
}

# validação simples
for k, v in {"SERPAPI_KEY": API_KEY, "DB_USER": DB_CONFIG["user"],
             "DB_PASSWORD": DB_CONFIG["password"], "DB_DSN": DB_CONFIG["dsn"]}.items():
    if not v:
        raise ValueError(f"Variável de ambiente ausente: {k}")

# =========================
# EXTRACT
# =========================

params = {
    "q": "taxa selic brasil",
    "hl": "pt",
    "gl": "br",
    "api_key": API_KEY
}

url = "https://serpapi.com/search.json"
data = requests.get(url, params=params).json()

# =========================
# LOAD (Oracle)
# =========================

conn = oracledb.connect(**DB_CONFIG)
cur = conn.cursor()

for r in data.get("organic_results", []):
    cur.execute("""
        INSERT INTO RAW_NOTICIAS (titulo, link, snippet, data_carga)
        VALUES (:1, :2, :3, :4)
    """, [r.get("title"), r.get("link"), r.get("snippet"), datetime.now()])

conn.commit()
cur.close()
conn.close()
