FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

RUN apt-get update

COPY requirements.txt /tmp/req.txt
RUN pip install -r /tmp/req.txt
