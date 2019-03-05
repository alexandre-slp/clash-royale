# Image
FROM python:alpine

# Installing necessary components
RUN apk add musl-dev gcc tzdata

# Adjust Time Zone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add files
COPY . /web

# Go to working directory
WORKDIR /web

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt