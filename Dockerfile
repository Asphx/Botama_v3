FROM python:3
RUN apt-get update -y && apt-get upgrade -y

RUN mkdir /app
COPY . /app
RUN "pip3 install -r /app/requirements.txt"

WORKDIR /app