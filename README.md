# Overview

*DISCLAIMER*: this project was only uploaded so I could show my work to others. This was also made in Seasons 3 and 4 of Fortnite, so I'm not sure if the API code will work as-is today. If you are interested in running your own version and need help, let me know and I'll do my best to assist.

Some friends and I were heavily into Fortnite a while back, and while our stats were available on FortniteTracker, I wanted a way to view all of our stats in one place. I also wanted a cool programming project that involved a variety of technologies such as containers and build systems. Using FortniteTracker's API, I created a simple leaderboard website using Python. Here's an overview of the project and my processes for developing & deploying it.

## Features

* Tracks Fortnite stats(games won, kills per match, etc.) for a group of players. Stats are separated by seasons, as well as lifetime stats.
* As players win games, new wins are announced in the win feed along with the time of the game and how many kills the player had in the game
** In a separate and slightly extended version of this application (not posted on GitHub), I made a simple API for the application. This allows us to query the stats database however we please. The API was created for a simple Discord bot that I made. The bot would announce new wins to the channel as they happened.

Here is how the stats are presented:

![Front Page](misc/leaderboard1_gh.png)

# How it works

1. FortniteTracker retrieves player stats directly from Epic Games' endpoints. Every 3 minutes, their site is updated with the latest stats. Luckily, they are kind enough to provide API access. All you need to do is create an account, log in, and generate an API key.
2. The leaderboard application runs in a Docker container on an AWS EC2 instance (running Ubuntu). AWS Elastic Container Registry handles anything related to the container: configuration, deployment, and image repository.
3. Every 5 minutes, a cronjob on the EC2 instance runs a script (dbupdate.py) inside of the container. This script queries FortniteTracker's API for player stats, and enters them in the local SQLite database

## Development and testing process

1. As changes are made to the code, new code is pushed to the development branch of the project's git repository on my local GitLab server
2. GitLab notifies my local Jenkins server of pushes to the development branch, and kicks off a build job on my local Docker server. This job stops the current running leaderboard container, builds a new container image with the latest code, and launches a container that is based off the new image
3. Since the application runs on port 80 on my Docker host, I simply connect to the hostname of my Docker host in a web browser and make sure everything is working. I should have included some sort of automated testing, but I'm still very much learning and will be soon implementing that in my new Flask project

## Production deployment process

1. Once changes are tested locally, I merge the development branch into the master branch in GitLab
2. GitLab notifies Jenkins of a merge into the master branch, and kicks off another job on the Docker host. This job builds the new production container image, pushes the new image to our image repository on AWS ECR, and tells our application to re-deploy itself with the latest production image. This causes the site to go down for about a minute, but since it only used by myself and a few friends, this was acceptable. More container instances running also means more money spent.

## Container information

The container is based off an Alpine Linux image with Python 3 ready to go. 