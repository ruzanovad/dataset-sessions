# Credit Score Dataset Experiments

This repository contains my experiments with the [Credit Score Classification dataset](https://www.kaggle.com/datasets/parisrohan/c redit-score-classification) and MLflow Tracking.

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
2. **Makefile** (GNU Make) *(optionally)*
3. **Python 3** *(optionally, because jupyter will be connected to jupyter server from docker container)*
4. **Jupyter Notebook** 

## Running

### Custom Docker Image

To avoid repeatedly downloading and installing the same packages each time you start a container, I created a custom Docker image with the required dependencies pre-installed. You can find the Dockerfile [here](./mlflow.Dockerfile).

Firstly, you need to build custom docker image, but all the pipeline is following:

```sh
make start run
```
## Additional Information

This project aims to streamline the process of experimenting with credit scoring models and tracking those experiments with MLflow. The use of Docker ensures a reproducible environment, while the custom Docker image reduces setup time.
