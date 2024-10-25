# Makefile

# Image name
IMAGE_NAME = fastapi-app

# Container name
CONTAINER_NAME = fastapi-app-container

# Port mapping
PORT = 8002

# Docker build
build:
	docker build -t $(IMAGE_NAME) .

# Docker run
run:
	docker run -d --name $(CONTAINER_NAME) -p $(PORT):8002 $(IMAGE_NAME)

# Docker stop
stop:
	docker stop $(CONTAINER_NAME)

# Docker remove container
rm-container:
	docker rm $(CONTAINER_NAME)

# Docker remove image
rm-image:
	docker rmi $(IMAGE_NAME)

# Docker logs
logs:
	docker logs -f $(CONTAINER_NAME)

# Docker shell access
shell:
	docker exec -it $(CONTAINER_NAME) /bin/sh

# Docker Compose up
compose-up:
	docker-compose up --build -d

# Docker Compose down
compose-down:
	docker-compose down

# Clean up all Docker containers, images, and volumes
clean:
	docker system prune -af --volumes

# Help
help:
	@echo "Makefile commands:"
	@echo "  build          Build the Docker image"
	@echo "  run            Run the Docker container in detached mode"
	@echo "  stop           Stop the running Docker container"
	@echo "  rm-container   Remove the Docker container"
	@echo "  rm-image       Remove the Docker image"
	@echo "  logs           View logs of the Docker container"
	@echo "  shell          Access shell in the running Docker container"
	@echo "  compose-up     Start services with Docker Compose"
	@echo "  compose-down   Stop services with Docker Compose"
	@echo "  clean          Remove unused containers, images, and volumes"

