FROM python:3.8-alpine

RUN apk update && \
    apk add build-base libpq jpeg-dev zlib-dev

RUN pip3 install --no-cache-dir -U pip wheel && \
    pip3 install --no-cache-dir sanic==22.6.0

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1