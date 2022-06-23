# syntax=docker/dockerfile:1
FROM python:3.9.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

EXPOSE 8000

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .