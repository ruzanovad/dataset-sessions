MLFLOW_SERVER_HOST = 0.0.0.0
MLFLOW_SERVER_PORT = 5000
MLFLOW_BACKEND_STORE_URI = postgresql://mlflow_user:magic_password@localhost/mlflow_db
MLFLOW_ARTIFACT_ROOT = data/mlruns

# 1. Create a virtual environment and install dependencies
.PHONY: setup
setup:
	@echo "Setting up virtual environment and installing dependencies..."
	@python3 -m venv venv
	@venv/bin/pip install --upgrade pip wheel setuptools
	venv/bin/pip install -r requirements.txt

# 2. Activate the virtual environment
.PHONY: activate
activate:
	@echo "Activating the virtual environment..."
	sh venv/bin/activate

# 1. Start MLflow server and dependencies
.PHONY: start
start:
	@echo "Starting MLflow server and dependencies..."
	sudo docker-compose up -d

# 2. Stop all services
.PHONY: stop
stop:
	@echo "Stopping MLflow server and dependencies..."
	sudo docker-compose down

# 4. Clean up environment (stop containers and remove volumes)
.PHONY: clean
clean:
	@echo "Cleaning up..."
	@sudo docker-compose down -v
	rm -rf data
# rm -rf venv

.PHONY: run
run:
	@echo "Running mlflow server..."
	@sudo docker-compose run mlflow

# Help target to list all available commands
.PHONY: help
help:
	@echo "Available make targets:"
	@echo "  setup             - Set up the virtual environment and install dependencies"
	@echo "  activate          - Activate the virtual environment"
	@echo "  start             - Start MLflow server and dependencies"
	@echo "  stop              - Stop all services"
	@echo "  run    		   - Run MLflow server"
	@echo "  clean             - Clean up Docker containers and volumes"
