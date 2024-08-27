# Makefile for managing the MLflow environment and Docker services

# 1. Create a virtual environment and install dependencies
.PHONY: setup
setup:
	@echo "Setting up virtual environment and installing dependencies..."
	@python3 -m venv .venv
	@.venv/bin/pip install --upgrade pip wheel setuptools
	@.venv/bin/pip install -r requirements.txt

# 2. Activate the virtual environment
.PHONY: activate
activate:
	@echo "Activating the virtual environment..."
	@sh .venv/bin/activate

# 3. Start MLflow server and dependencies using Docker Compose
.PHONY: start
start:
	@echo "Starting MLflow server and dependencies..."
	@sudo docker compose up -d

# 4. Stop all Docker services
.PHONY: stop
stop:
	@echo "Stopping MLflow server and dependencies..."
	@sudo docker compose down -v

# 5. Clean up environment (remove Docker volumes and virtual environment)
.PHONY: clean
clean:
	@echo "Cleaning up environment..."
	@sudo docker compose down -v
	@rm -rf data
	@rm -rf .venv

# 6. Run MLflow server in a Docker container
.PHONY: run
run:
	@echo "Running MLflow server..."
	@sudo docker compose run mlflow

# 7. Docker diagnosis: display container, volume, and image information
.PHONY: diagnosis
diagnosis:
	@echo "Displaying Docker diagnostic information..."
	sudo docker ps
	sudo docker volume ls
	sudo docker images

# 8. Help target to list all available commands
.PHONY: help
help:
	@echo "Available make targets:"
	@echo "  setup             - Set up the virtual environment and install dependencies"
	@echo "  activate          - Activate the virtual environment"
	@echo "  start             - Start MLflow server and dependencies using Docker Compose"
	@echo "  stop              - Stop all Docker services"
	@echo "  clean             - Clean up Docker containers, volumes, and the virtual environment"
	@echo "  run               - Run MLflow server in a Docker container"
	@echo "  diagnosis         - Display Docker container, volume, and image information"
