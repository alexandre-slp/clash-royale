# Image
FROM python:alpine

# Installing necessary components
RUN apk add musl-dev gcc tzdata pipenv

# Adjust Time Zone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add files
COPY . /web

# Go to working directory
WORKDIR /web

# Install requirements
RUN pipenv install
