FROM python:3.8

RUN apt-get update && \
    apt install -y netcat

RUN pip install --no-cache-dir -U pip wheel && \
    pip install --no-cache-dir django==3.2.14 \
        djangorestframework==3.13.1

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1