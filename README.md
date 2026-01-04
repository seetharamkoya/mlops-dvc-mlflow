# Dvc (Data versioning)
Demo project to track the dataset tracking using dvc.

## Python venv & dvc instllation & dataset versioning
1. python -m venv .venv
2. source .venv/Scripts/activate
3. python -m pip install dvc
4. dvc init
5. dvc add data/raw/iris.csv (To Add your dataset to DVC (.dvc))
6. dvc remote add -d mlops-demo s3://mlops-demo-dvc-ksr (To Configure remote storage)
7. python -m pip install dvc_s3
8. dvc push ( It will push to aws s3)
9. dvc pull (To pull latest Dataset version)


## Dependencies
1. dvc install
2. Storage (AWS, AZURE, GCP, local storage)
3. aws configure
4. dvc_s3


# Mlflow (Experiment Tracking)

