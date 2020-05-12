# Webapp-with-docker
A simple webapp with database using dockerfile

SETTING UP AND BUILDING IMAGE:

Clone the repository

Chanege workdir to Webapp-with-docker

-  cd /Webapp-with-docker

Build docker image with the following command

-  docker build -t flaskapp:v1 .

CREATING A CONTAINER :

docker run -d --name <name of container> -p <port you want to user>:5000 flask:v1

Eg - docker run -d --name app -p 55111:5000 flask:v1


