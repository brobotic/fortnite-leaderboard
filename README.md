# Overview

*DISCLAIMER*: this project was only uploaded so I could show my work to others. If you'd like to use this for your own purposes, let me know and I'll help you out.

Some friends and I were heavily into Fortnite a while back, and while our stats were available on FortniteTracker, I wanted a way to view all of our stats in one place. Using FortniteTracker's API, I created a simple leaderboard website using Python. Here's an overview of the project and my processes for developing & deploying it.

## Features

* Tracks Fortnite stats(games won, kills per match, etc.) for a group of players. Stats are separated by seasons, as well as lifetime stats
* As players win games, new wins are announced in the win feed along with the time of the game and how many kills the player had in the game
** In a separate and slightly extended version of this application (not posted on GitHub), I made a simple API for the application. This allows us to query the stats database however we please. The API was created for a simple Discord bot that I made. The bot would announce new wins to the channel as they happened

Here is how the stats are presented:

![Front Page](misc/leaderboard1_gh.png)

# How it works

1. FortniteTracker somehow retrieves player stats directly from Epic Games' endpoints. Every 3 minutes, their site is updated with the latest stats. Luckily, they are kind enough to provide API access. All you need to do is create an account, log in, and generate an API key
2. The leaderboard application runs on an AWS EC2 instance inside of a Docker container. AWS Elastic Container Registry handles anything related to the container: configuration, deployment, as well as the image repository. As new code is merged into the master branch in GitLab, a Jenkins job is kicked off that re-deploys the latest container image to AWS
3. Every 5 minutes, a cronjob on the EC2 instance runs a script (dbupdate.py) inside of the container. This script queries FortniteTracker's API for player stats, and enters them in our local SQLite database

## Development and testing process

1. As features are implemented and/or bugs are fixed, new code is pushed to the development branch of the project's repository on my local GitLab server
2. GitLab informs my local Jenkins server of pushes to the development branch, and kicks off a build job on my local Docker server. This job stops any running containers, builds a new container image with the latest code, and launches a container that is based off the new image
3. Since the application runs on port 80 on my Docker host, I simply connect to the hostname of my Docker host in a web browser

## Production deployment process

1. Once changes are tested locally, we merge the development branch into the master branch in GitLab
2. GitLab informs Jenkins of a merge into the master branch, and kicks off another job on the Docker host. This job builds the new production container image, pushes the new image to our image repository on AWS ECR, and tells our application to re-deploy itself with the latest production image
