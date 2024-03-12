FROM python:3.12-alpine

# set environment variables
RUN mkdir /telegram/
WORKDIR /telegram
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY .. .
