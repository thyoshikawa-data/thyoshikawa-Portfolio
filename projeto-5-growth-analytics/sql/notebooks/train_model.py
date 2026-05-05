import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from feature_engineering import build_features
import joblib

df = pd.read_csv("../data/raw.csv")

features = build_features(df)

# TARGET (igual seu código)
features['target_7d'] = (features['recency'] <= 7).astype(int)
features['target_30d'] = (features['recency'] <= 30).astype(int)

X = features[['recency', 'frequency', 'monetary']]

model_7d = RandomForestClassifier()
model_7d.fit(X, features['target_7d'])

model_30d = RandomForestClassifier()
model_30d.fit(X, features['target_30d'])

joblib.dump(model_7d, "model_7d.pkl")
joblib.dump(model_30d, "model_30d.pkl")
