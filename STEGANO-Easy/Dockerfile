FROM python:3.11-slim

RUN pip install flask

WORKDIR /app

COPY app.py .
COPY stego.png .

EXPOSE 8000

CMD ["python", "app.py"]
