import pandas as pd
from serpapi import GoogleSearch
from datetime import datetime
import time

# ==========================================
# CONFIG
# ==========================================

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

DATE_RANGE = "today 12-m"
GEO = "BR"

# ==========================================
# SEARCH GROUPS
# ==========================================

SEARCH_GROUPS = {

    "SUV": [
        "Jeep SUV Brasil",
        "Toyota SUV Brasil",
        "Volkswagen SUV Brasil",
        "Honda SUV Brasil",
        "Chevrolet SUV Brasil",
        "Hyundai SUV Brasil"
    ],

    "SEDAN": [
        "Toyota Sedan Brasil",
        "Honda Sedan Brasil",
        "Volkswagen Sedan Brasil",
        "Chevrolet Sedan Brasil",
        "Hyundai Sedan Brasil"
    ],

    "HATCH": [
        "Volkswagen Hatch Brasil",
        "Fiat Hatch Brasil",
        "Chevrolet Hatch Brasil",
        "Hyundai Hatch Brasil",
        "Renault Hatch Brasil"
    ],

    "ELETRICOS": [
        "BYD Brasil",
        "GWM Brasil",
        "Volvo Elétrico Brasil",
        "Toyota Híbrido Brasil",
        "CAOA Chery Elétrico"
    ],

    "CAMINHOES": [
        "Scania Caminhões Brasil",
        "Volvo Trucks Brasil",
        "Mercedes-Benz Caminhões",
        "DAF Caminhões Brasil",
        "Volkswagen Caminhões"
    ]
}

# ==========================================
# DATE PARSER
# ==========================================

def parse_trend_date(date_str):

    if pd.isnull(date_str):
        return None

    try:

        start_date = str(date_str).split('–')[0].strip()

        return pd.to_datetime(start_date)

    except:
        return None

# ==========================================
# INGESTION
# ==========================================

all_data = []

for category, searches in SEARCH_GROUPS.items():

    print(f"\n🚀 Categoria: {category}")

    for term in searches:

        print(f"🔎 Coletando: {term}")

        try:

            params = {
                "engine": "google_trends",
                "q": term,
                "geo": GEO,
                "date": DATE_RANGE,
                "api_key": SERPAPI_KEY
            }

            search = GoogleSearch(params)

            results = search.get_dict()

            timeline = results.get(
                "interest_over_time",
                {}
            ).get(
                "timeline_data",
                []
            )

            for item in timeline:

                all_data.append({
                    "trend_date": item.get("date"),
                    "search_term": term,
                    "category": category,
                    "interest_score": item.get(
                        "values",
                        [{}]
                    )[0].get("value"),
                    "load_date": datetime.now()
                })

            print(f"✅ {term} coletado")

            # evita rate limit
            time.sleep(2)

        except Exception as e:

            print(f"❌ Erro em {term}: {e}")

# ==========================================
# DATAFRAME
# ==========================================

df = pd.DataFrame(all_data)

# ==========================================
# DATA TREATMENT
# ==========================================

df['trend_date'] = df['trend_date'].apply(
    parse_trend_date
)

# remove datas inválidas
df = df[df['trend_date'].notnull()]

# remove interest_score nulo
df = df[df['interest_score'].notnull()]

# converte score
df['interest_score'] = pd.to_numeric(
    df['interest_score'],
    errors='coerce'
)

# remove possíveis nulos
df = df[df['interest_score'].notnull()]

# ordenação
df = df.sort_values(
    ['category', 'search_term', 'trend_date']
)

# reset index
df = df.reset_index(drop=True)

# ==========================================
# EXPORT
# ==========================================

OUTPUT_FILE = "../data/automotive_market_trends.csv"

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\n✅ CSV exportado com sucesso!")
print(f"📁 Arquivo: {OUTPUT_FILE}")

# ==========================================
# KPIs
# ==========================================

print("\n📊 Registros coletados:")
print(len(df))

print("\n📈 Categorias:")
print(df['category'].value_counts())

print("\n🏆 Top marcas:")
print(
    df.groupby('search_term')['interest_score']
      .mean()
      .sort_values(ascending=False)
      .head(10)
)
