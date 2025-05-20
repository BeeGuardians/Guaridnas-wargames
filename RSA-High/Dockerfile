FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY app.py .
COPY public.pem .
COPY ciphertext.txt .

# Flask 설치
RUN pip install --no-cache-dir flask

# 컨테이너 포트 오픈
EXPOSE 8000

# 앱 실행
CMD ["python", "app.py"]
