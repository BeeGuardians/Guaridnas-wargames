FROM python:3.9-slim

WORKDIR /app

COPY app.py flag.txt /app/

RUN pip install flask

EXPOSE 8000

CMD ["python", "app.py"]
