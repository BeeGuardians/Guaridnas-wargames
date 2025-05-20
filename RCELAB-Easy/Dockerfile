FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    iputils-ping \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install flask

COPY app.py .
COPY flag.txt .

EXPOSE 8000

CMD ["python", "app.py"]
