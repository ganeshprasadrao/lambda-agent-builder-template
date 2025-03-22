#!/bin/bash

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Generate environment variables
echo "Generating environment variables..."
./scripts/generate_env.sh

# Stop and remove all existing containers from previous deployment
docker-compose down || true

# Copy the deployment docker-compose file to the standard name
cp docker-compose-deploy.yml docker-compose.yml

# Pull the latest images
echo "Pulling latest images..."
docker-compose pull

# Start the application using Docker Compose
echo "Starting all services with docker-compose..."
docker-compose up -d

# Clean up old images
echo "Cleaning up old images..."
docker image prune -af

# Check if all services are running
echo "Checking service status..."
docker-compose ps

# Start any stopped containers (if needed)
stopped_containers=$(docker ps -q -f status=exited)
if [ ! -z "$stopped_containers" ]; then
    echo "Starting stopped containers..."
    for container_id in $stopped_containers; do
        docker start $container_id
    done
fi

echo "Deployment completed successfully!"
