#!/bin/bash

# Update the system
yum update -y

# Install or update Docker if needed
if ! command -v docker &>/dev/null; then
    amazon-linux-extras install docker -y
    systemctl enable docker
    systemctl start docker
fi

# Install Docker Compose if not present or update it
if ! command -v docker-compose &>/dev/null; then
    curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    ln -sf /usr/local/bin/docker-compose /usr/bin/docker-compose
fi

# Create a directory for environment variables if it doesn't exist
mkdir -p /home/ec2-user/env

# Make sure the deployment directory exists
mkdir -p /home/ec2-user/$FOLDER_NAME

# Clean up any previous failed deployments
if [ -f /home/ec2-user/$FOLDER_NAME/docker-compose.yml ]; then
    cd /home/ec2-user/$FOLDER_NAME
    docker-compose down || true
fi 