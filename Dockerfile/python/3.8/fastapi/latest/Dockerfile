FROM python:3.8

RUN apt-get update && \
    apt install -y netcat && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -U pip wheel fastapi

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1