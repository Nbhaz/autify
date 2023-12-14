#!/bin/bash

# Define variables
IMAGE_NAME="autify-nithin"
CONTAINER_NAME="autify-nithin-cn"

# Build Docker image
docker build -t $IMAGE_NAME .

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Docker image build successful"

    # Run Docker container with arguments
    docker run --name $CONTAINER_NAME -v ${PWD}:/app "$IMAGE_NAME" "$@"

    # Clean up - remove the container after it exits
    docker container rm $CONTAINER_NAME
else
    echo "Docker image build failed"
fi
