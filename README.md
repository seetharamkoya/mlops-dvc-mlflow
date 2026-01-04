# Data Version Control (DVC)
DVC to track the dataset version.

## STEP:1
### Python venv & dvc instllation & dataset versioning
1. python -m venv .venv
2. source .venv/Scripts/activate
3. python -m pip install dvc
4. dvc init
5. dvc add data/raw/iris.csv (To Add your dataset to DVC (.dvc))
6. dvc remote add -d mlops-demo s3://mlops-demo-dvc-ksr (To Configure remote storage)
7. python -m pip install dvc_s3
8. dvc push ( It will push to aws s3)
9. dvc pull (To pull latest Dataset version)


### Dependencies
1. dvc install
2. Storage (AWS, AZURE, GCP, local storage)
3. aws configure
4. dvc_s3

## STEP:2
# Experiment Tracking (MLflow)
Experiment tracking is the process of recoding of all machine learning trainings/runs. So that you can compare different models, reproduce or choose the best model accuracy.

### Experiment Tracking System stores
1. Parameters
2. Code Version
3. Dataset version
4. Metrics
5. Artifacts
6. System info

MLflow is an open-source MLOps framework used to manage the end-to-end machine learning lifecycle.
It helps you track experiments, manage models, and make ML work reproducible.

