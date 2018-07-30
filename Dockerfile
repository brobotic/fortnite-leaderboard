# Used for the production container image that runs on AWS, built in deploy.sh

# We use Alpine Linux (with python3 configured) to keep our base image small. We can't just use a python3 base image, because we still need the functionality of an operating system since we need to configure other packages like nginx(web server) and supervisor(process controller for our python application)
FROM frolvlad/alpine-python3:latest

# Our application will live in the /app directory inside the  container
WORKDIR /app

# Copy all of our project files to /app
ADD . /app

# Create directory structure for configurations. Can't remember why creating /run/nginx is necessary
RUN mkdir -p /run/nginx/
RUN mkdir /etc/supervisor.d/

# Create a new user so our application runs as an unprivileged user, and make it the owner of our application directory
RUN adduser -D -g '' fortnite
RUN chown -R fortnite:root /app

# Copy our LetsEncrypt certificates and supervisord configuration
COPY supervisor.ini /etc/supervisor.d/supervisor.ini
COPY nginx/cert.pem /etc/ssl/certs/cert1.pem
COPY nginx/privkey.pem /etc/ssl/certs/privkey1.pem

# Update all system packages
RUN apk update

# Install nginx
RUN apk add nginx

# Copy over nginx config
ADD nginx/fortnite.conf /etc/nginx/conf.d/

# Install supervisord
RUN apk add supervisor

# Install all of the python dependencies that our project requires to run
RUN pip install -r requirements.txt

# I think this is old and can be removed. In production, our application runs on port 5000 (see supervisor.ini) and nginx proxies port 5000 to port 443 (see nginx/fortnite.conf)
EXPOSE 80

# Finally, launcher supervisord with our configuration file (which will run our application as a process in the background)
CMD ["supervisord","--nodaemon","-c","/etc/supervisord.conf"]