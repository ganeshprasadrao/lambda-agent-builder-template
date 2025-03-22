#!/bin/bash

cd /home/ec2-user/$FOLDER_NAME

# Ensure all services are running
docker-compose ps
docker-compose up -d

# Check if main app container is running
app_container=$(docker-compose ps -q app)
if [ -z "$app_container" ]; then
    echo "Error: Main application container failed to start"
    exit 1
fi

# Check if celery worker is running
celery_container=$(docker-compose ps -q celery_worker)
if [ -z "$celery_container" ]; then
    echo "Error: Celery worker container failed to start"
    exit 1
fi

# Check if RabbitMQ is running
rabbitmq_container=$(docker-compose ps -q rabbitmq)
if [ -z "$rabbitmq_container" ]; then
    echo "Error: RabbitMQ container failed to start"
    exit 1
fi

echo "All services are running successfully!" 