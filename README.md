# Overview

Some friends and I were heavily into Fortnite a while back, and while our stats were available on FortniteTracker, I wanted a way to view all of our stats in one place. Using FortniteTracker's API, I created a simple leaderboard website using Python. Here's an overview of the project and my processes for developing & deploying it.

## How it works

TODO


## Development process

1. As features are implemented and/or bugs are fixed, new code is pushed to the development branch of the project's repository on my local GitLab server
2. GitLab informs my local Jenkins server of pushes to the development branch, and kicks off a build job on my local Docker server
