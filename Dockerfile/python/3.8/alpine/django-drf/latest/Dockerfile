FROM python:3.8-alpine

RUN apk update && \
    apk add build-base libpq jpeg-dev zlib-dev

RUN pip3 install --no-cache-dir -U pip wheel djangorestframework && \
    pip3 install --no-cache-dir django==3.2.14

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1