FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

RUN apt-get update

COPY ../requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
