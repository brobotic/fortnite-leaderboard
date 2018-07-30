#!/bin/bash

# 1. When we are ready to test our changes, we push our latest changes to the 'dev' branch in GitLab
# 2. GitLab informs Jenkins of new code via webhook, which fires off a Jenkins build job
# 3. Jenkins tells the build agent (a local CentOS 7 server running Docker) to pull down the latest code and run build.sh
# 3a. The build job copies the latest version of the database file from another directory to the build direcotry
# 3b. Every hour, we rsync the production database file from the AWS instance to our local Docker server so we can always test with (just about) the latest data
# 4. build.sh looks for running containers (of the same project type) and stops them
# 5. build.sh builds a new Docker image with the latest code (using Dockerfile.dev)
# 6. build.sh runs the new container image, and maps port 80 on the container to port 80 on the Docker server
# 7. Now we can test our application in our development environment before pushing changes to AWS (see deploy.sh for that)

CONTAINER=$(docker ps | grep "Up" | grep "supervisor" | awk '{print $1}')

if [[ $CONTAINER ]]; then
    docker stop $CONTAINER
else
    echo "No containers running."
fi

docker build -t fortnitefriends -f Dockerfile.dev .

docker run -d -p 80:80 fortnitefriends