import pandas as pd
import yaml
import joblib
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# -------------------------
# Load parameters
# -------------------------
with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

model_params = params["model"]

# -------------------------
# Load data
# -------------------------
df = pd.read_csv("data/raw/iris.csv")

X = df.drop("species", axis=1)
y = df["species"]

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -------------------------
# MLflow configuration
# -------------------------
mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("iris-demo")

# -------------------------
# Training + Tracking
# -------------------------
with mlflow.start_run(run_name="logistic-regression"):

    # Log all hyperparameters at once
    mlflow.log_params(model_params)

    model = LogisticRegression(
        C=model_params["C"],
        max_iter=model_params["max_iter"]
    )

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # Log metrics
    mlflow.log_metric("accuracy", acc)

    # Log model to MLflow
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name=None
    )

    # Save model locally for DVC / deployment
    joblib.dump(model, "models/model.joblib")

    print(f"Accuracy: {acc:.4f}")
