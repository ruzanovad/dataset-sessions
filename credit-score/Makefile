# Targets


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

# 3. Run experiment in the Python container
.PHONY: run
run:
	@echo "Running MLflow experiment..."
	sudo docker-compose run --rm python bash -c "pip install -r requirements.txt"

# 4. Clean up environment (stop containers and remove volumes)
.PHONY: clean
clean:
	@echo "Cleaning up..."
	@sudo docker-compose down -v
	rm -rf ./data

# Help target to list all available commands
.PHONY: help
help:
	@echo "Available make targets:"
	@echo "  setup             - Set up the Docker environment (build containers and start services)"
	@echo "  start             - Start MLflow server and dependencies"
	@echo "  stop              - Stop all services"
	@echo "  run    		   - Run MLflow experiment"
	@echo "  clean             - Clean up Docker containers and volumes"
