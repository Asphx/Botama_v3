FROM python:3
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python3-pip build-essential libssl-dev libffi-dev python-dev -y 
RUN mkdir /app
COPY . /app
RUN cd /app
RUN "pip3 install -r /app/requirements.txt"

WORKDIR /app
