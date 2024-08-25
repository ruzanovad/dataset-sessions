# Credit Score Dataset Experiments

This repository contains my experiments with the [Credit Score Classification dataset](https://www.kaggle.com/datasets/parisrohan/credit-score-classification) and MLflow Tracking.

## Project Structure

### 1. Exploratory Data Analysis (EDA)
- Explore the data and gain insights through EDA. 
  - [View EDA](./eda)

### 2. Experiments
- Various machine learning experiments using the dataset.
  - [View Experiments](./experiments)

## Requirements

To reproduce the experiments, you will need the following tools installed:

1. **Docker** (v3+)
2. **Makefile** (GNU Make)
3. **Python 3**
4. **Jupyter Notebook** 

## Installation

To set up the required Python packages for the project, you can export them to a `requirements.txt` file using the following command:

```bash
pip list --format=freeze --local | grep -E "^(pandas|matplotlib|numpy|scikit-learn|seaborn|mlflow|pickleshare|ipykernel|psycopg2|dash)==" > requirements.txt
```

## Docker Troubleshooting

This project uses PostgreSQL as the backend for MLflow. The default MLflow Docker image does not include the required PostgreSQL dependencies, so you'll need to install them manually. This includes `psycopg2`, which requires [`pg_config`](https://stackoverflow.com/questions/11618898/pg-config-executable-not-found)).

To start the MLflow server with PostgreSQL support, run the following command:

```bash
sh -c "apt update && \
      apt install -y gcc libpq-dev && \
      pip install psycopg2 && \
      mlflow server \
      --backend-store-uri postgresql://mlflow_user:magical_password@postgres/mlflow_db \
      --default-artifact-root /mlflow/artifacts \
      --host 0.0.0.0 \
      --port 5000"
```

### Custom Docker Image

To avoid repeatedly downloading and installing the same packages each time you start a container, I created a custom Docker image with the required dependencies pre-installed. You can find the Dockerfile [here](./mlflow.Dockerfile).

## Additional Information

This project aims to streamline the process of experimenting with credit scoring models and tracking those experiments with MLflow. The use of Docker ensures a reproducible environment, while the custom Docker image reduces setup time.
