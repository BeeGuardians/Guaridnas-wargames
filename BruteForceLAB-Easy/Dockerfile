FROM python:3.11-slim

WORKDIR /app

# Flask 설치
RUN pip install flask

# 앱 및 플래그 파일 복사
COPY app.py .
COPY flag.txt .
COPY passwords.txt .

EXPOSE 8000

CMD ["python", "app.py"]
