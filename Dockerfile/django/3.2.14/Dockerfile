FROM python:3.8-alpine

RUN apk update \
    && apk add build-base

RUN mkdir /usr/src/app

WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app

RUN pip3 install --no-cache-dir django==3.2.14
