FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

WORKDIR /workspace

EXPOSE 8000

RUN apt-get update

COPY requirements.txt /tmp/req.txt

RUN pip install -r /tmp/req.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]