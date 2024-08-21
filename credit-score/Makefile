# Targets


# 2. Start MLflow server and dependencies
.PHONY: start
start:
	@echo "Starting MLflow server and dependencies..."
	docker-compose up -d

# 2. Stop all services
.PHONY: stop
stop:
	@echo "Stopping MLflow server and dependencies..."
	docker-compose down

# 3. Run experiment in the Python container
.PHONY: run-experiment
run-experiment:
	@echo "Running MLflow experiment..."
	docker-compose run --rm python bash -c "pip install -r requirements.txt && python run_experiment.py"

# 4. Clean up environment (stop containers and remove volumes)
.PHONY: clean
clean:
	@echo "Cleaning up..."
	@docker-compose down -v
	rm -rf ./data

# Help target to list all available commands
.PHONY: help
help:
	@echo "Available make targets:"
	@echo "  setup             - Set up the Docker environment (build containers and start services)"
	@echo "  start             - Start MLflow server and dependencies"
	@echo "  stop              - Stop all services"
	@echo "  run-experiment    - Run MLflow experiment"
	@echo "  clean             - Clean up Docker containers and volumes"
