FROM python:3.11-slim

# 시스템 패키지 설치 (sqlite3 포함)
RUN apt-get update && apt-get install -y \
    sqlite3 \
 && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /app

# Python 패키지 설치
RUN pip install flask

# 앱 코드 복사
COPY app.py .
COPY flag.txt .

# 포트 노출
EXPOSE 8000

# 앱 실행
CMD ["python", "app.py"]
