import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

df = pd.read_csv("data/raw/iris.csv")
X = df.drop("species", axis=1)
y = df["species"]

model = joblib.load("models/model.joblib")
preds = model.predict(X)

print("Evaluation complete")