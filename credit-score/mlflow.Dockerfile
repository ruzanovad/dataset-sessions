FROM ghcr.io/mlflow/mlflow:v2.15.1

RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    pip install psycopg2


ENV MLFLOW_TRACKING_URI=http://0.0.0.0:5000

EXPOSE 5000

CMD ["mlflow", "server", \
    "--backend-store-uri", "postgresql://mlflow_user:magical_password@postgres/mlflow_db", \
    "--default-artifact-root", "/mlflow/artifacts", \
    "--host", "0.0.0.0", \
    "--port", "5000"]