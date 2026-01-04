# mlops-dvc-mlflow
Demo project to track the dataset tracking using dvc.

## python venv & dvc instllation & dataset tracking
1. python -m venv .venv
2. source .venv/Scripts/activate
3. python -m pip install dvc
4. dvc init
5. dvc add data/raw/iris.csv (it will add .dvc file to the dataset folder)
6. dvc remote add -d mlops-demo s3://mlops-demo-dvc-ksr (This will update the config file for the dataset reference)
7. python -m pip install dvc_s3
8. dvc push ( It will push to aws s3)


## Dependencies
1. dvc install
2. Cloud storage (AWS, AZURE, GCP)
3. aws configure
4. dvc_s3
