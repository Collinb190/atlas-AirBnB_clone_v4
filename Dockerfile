# Use Ubuntu as the base image
FROM ubuntu:20.04

# Install curl, Node.js 14, request, and semistandard globally
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    npm install semistandard --global && \
    npm install request --global

# Install python dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip \
    python3-lxml \
    mysql-client && \
    pip3 install \
    flask \
    flask_cors \
    flasgger \
    jsonschema==3.0.1 \
    pathlib2 \
    sqlalchemy && \
    echo 'export PS1="${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@\h\[\033[00m\]\[\033[01;34m\][\[\033[00m\]\[\033[01;33m\]\W\[\033[00m\]\[\033[01;34m\]]\[\033[00m\]\$ "' >> /root/.bashrc


# Set environment variables for MySQL
ENV HBNB_MYSQL_USER=hbnb_dev
ENV HBNB_MYSQL_PWD=hbnb_dev_pwd
ENV HBNB_MYSQL_HOST=localhost
ENV HBNB_MYSQL_DB=hbnb_dev_db
ENV HBNB_TYPE_STORAGE=db

# Expose port 5001 for Flask app
EXPOSE 5001

# Create a directory for your project in the container
WORKDIR /app

# Copy the contents of your local folder into the container
COPY . /app

# Set the default command to be executed when the container starts
CMD ["/bin/bash"]
