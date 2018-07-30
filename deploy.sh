#!/bin/bash

# 1. When we're ready to deploy, we merge the 'Dev' branch in GitLab into the 'Master' branch
# 2. GitLab informs Jenkins of the merge via webhook, which fires off a Jenkins build job
# 3. Jenkins tells the build agent (a local CentOS 7 server running Docker) to pull down the latest code and run deploy.sh
# 4. deploy.sh builds the production container image with the latest code (using Dockerfile)
# 5. deploy.sh authenticates with AWS Elastic Container Registry
# 6. deploy.sh tags the newly built production container as the latest version of the image
# 7. deploy.sh pushes the new production container image to AWS ECR
# 8. deploy.sh tells our application service to re-deploy itself with the latest production image

docker build -t fortnitefriends .
$(~/.local/bin/aws ecr get-login --no-include-email --region us-west-2)
docker tag fortnitefriends:latest 098857454472.dkr.ecr.us-west-2.amazonaws.com/fortnitefriends:latest
docker push 098857454472.dkr.ecr.us-west-2.amazonaws.com/fortnitefriends:latest
/home/jenkins/.local/bin/aws ecs update-service --cluster default --service fortnitefriends --force-new-deployment