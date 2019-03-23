# Image
FROM python:alpine

# Installing necessary components
RUN apk add musl-dev gcc tzdata

# Adjust Time Zone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add files
COPY . /dash

# Go to working directory
WORKDIR /dash

# Install requirements
RUN pip install pipenv
RUN pipenv install
