#!/bin/bash

# Start Jupyter Notebook in the background
jupyter notebook --notebook-dir=. --ip='0.0.0.0' --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''&

# Start MLflow server
mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri postgresql://mlflow_user:magical_password@postgres/mlflow_db --default-artifact-root /app/mlflow_artifacts
