#!/bin/bash

cd /home/ec2-user/$FOLDER_NAME

# Define the health check endpoint we just added
HEALTH_CHECK_URL="http://localhost:8000/health"

# Wait for the API to become available (up to 60 seconds)
echo "Waiting for API to become available..."
for i in {1..12}; do
    response=$(curl -s "$HEALTH_CHECK_URL")
    if echo "$response" | grep -q "healthy"; then
        echo "API is up and running!"
        break
    fi
    
    if [ $i -eq 12 ]; then
        echo "Error: API failed to start within the expected time"
        echo "Last response from server: $response"
        exit 1
    fi
    
    echo "Waiting for API to start... (attempt $i/12)"
    sleep 5
done

# Check that all containers are healthy
echo "Checking container health..."
for service in app celery_worker rabbitmq; do
    container_id=$(docker-compose ps -q $service)
    
    if [ -z "$container_id" ]; then
        echo "Error: $service container is not running"
        exit 1
    fi
    
    container_status=$(docker inspect --format='{{.State.Status}}' $container_id)
    if [ "$container_status" != "running" ]; then
        echo "Error: $service container is not running. Status: $container_status"
        exit 1
    fi
    
    # For RabbitMQ, check if management interface is responding
    if [ "$service" = "rabbitmq" ]; then
        if ! curl -s -o /dev/null -w "%{http_code}" "http://localhost:15672/" | grep -q "200\|302"; then
            echo "Warning: RabbitMQ management interface is not responding"
        else
            echo "RabbitMQ management interface is accessible"
        fi
    fi
done

echo "Validation complete: All services are healthy and running!" 