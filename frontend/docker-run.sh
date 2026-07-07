#!/bin/bash

#Check if the frontend image already exists
if [[ "$(docker images -q faraja-frontend 2> /dev/null)" == "" ]]; then
    echo "Building frontend image..."
    docker build -t faraja-frontend .
fi

#Check if the network exists, create it if not
if ! docker network inspect faraja-network &> /dev/null; then
    echo "Creating faraja-network..."
    docker network create faraja-network
fi

#Stop and remove existing container if it exists
if docker ps -a | grep -q faraja-frontend; then
    echo "Removing existing frontend container..."
    docker stop faraja-frontend 2> /dev/null
    docker rm faraja-frontend 2> /dev/null
fi

#Run the frontend container
echo "Starting frontend container..."
docker run -d \
    --name faraja-frontend \
    --network faraja-network \
    -p 3001:3001 \
    -e NEXT_PUBLIC_API_URL=http://backend:8000 \
    faraja-frontend

echo "Frontend container started successfully"
echo "Access at: http://localhost:3001"
echo ""
echo "Useful commands:"
echo "  View logs:    docker logs faraja-frontend"
echo "  Stop:         docker stop faraja-frontend"
echo "  Start:        docker start faraja-frontend"
echo "  Remove:       docker rm faraja-frontend"
