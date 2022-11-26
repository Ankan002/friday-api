FROM ubuntu:22.04

WORKDIR /usr/friday-api

ENV PORT ${PORT}
ENV PY_ENV ${PY_ENV}

ENV DEBIAN_FRONTEND noninteractive

SHELL ["/bin/bash", "-c"]

RUN apt update

RUN apt-get install -y python3

RUN apt-get install -y python3-pip

RUN apt-get install -y build-essential

COPY requirements.txt .

RUN ["pip3", "install", "-r", "requirements.txt"]

COPY . .

EXPOSE ${PORT}

CMD python3 -m uvicorn main:app --host 0.0.0.0 --port ${PORT}