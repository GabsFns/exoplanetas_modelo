import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/dataset_features.csv")
df = df.replace('——', 0)
df = df.apply(pd.to_numeric, errors='coerce')

df = df.dropna()
x = df.drop("label", axis=1)
y = df["label"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(x_train, y_train)

joblib.dump(modelo, "models/modelo_rf.pkl")

print("Modelo treinado e salvo.")