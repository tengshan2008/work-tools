FROM python:3.8-slim

RUN apt-get update && \
    apt install -y netcat

RUN pip install --no-cache-dir -U pip wheel && \
    pip install --no-cache-dir sanic==22.6.0

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1