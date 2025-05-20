FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y \
    gcc libc6-dev socat \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY vulnerable.c .
COPY flag.txt .
COPY start.sh .

RUN gcc -no-pie -fno-stack-protector -o vuln vulnerable.c && \
    chmod 444 flag.txt

EXPOSE 8000

CMD ["bash", "start.sh"]
