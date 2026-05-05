import pandas as pd
import oracledb

df = pd.read_csv("predictions.csv")

conn = oracledb.connect(
    user="SEU_USER",
    password="SUA_SENHA",
    dsn="oracle.fiap.com.br:1521/ORCL"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO REFINED_PREDICTIONS 
        (fk_contact, prob_compra_7d, prob_compra_30d, rota_prevista)
        VALUES (:1, :2, :3, :4)
    """, [
        row['fk_contact'],
        float(row['prob_compra_7d']),
        float(row['prob_compra_30d']),
        row['rota_prevista']
    ])

conn.commit()
cursor.close()
conn.close()
