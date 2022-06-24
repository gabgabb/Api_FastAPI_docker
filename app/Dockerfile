# syntax=docker/dockerfile:1
FROM python:3.9.13
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

EXPOSE 80

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "server.app:FestivalUserAPI", "--host", "0.0.0.0", "--port", "80"]