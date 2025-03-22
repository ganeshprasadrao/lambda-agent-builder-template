#!/bin/bash

# This script will be used to extract environment variables from AWS Parameter Store or Secrets Manager
# and create the necessary environment files for Docker Compose

cd /home/ec2-user/$FOLDER_NAME

# Create env file for Docker Compose
cat > .env << EOL
DATABASE_URL=${DATABASE_URL}
MY_GITHUB_TOKEN=${MY_GITHUB_TOKEN}
PERPLEXITY_API_KEY=${PERPLEXITY_API_KEY}
GROQ_API_KEY=${GROQ_API_KEY}
DEEPSEEK_API_KEY=${DEEPSEEK_API_KEY}
HUGGINGFACE_API_KEY=${HUGGINGFACE_API_KEY}
HYPERBOLIC_API_KEY=${HYPERBOLIC_API_KEY}
TOGETHER_API_KEY=${TOGETHER_API_KEY}
AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
EOL

# Set proper permissions
chmod 600 .env

echo "Environment variables file generated successfully" 