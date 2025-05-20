from flask import Flask, request
import random

app = Flask(__name__)

# 랜덤 비밀번호 선택
with open("passwords.txt") as f:
    PASSWORD_LIST = [line.strip() for line in f.readlines()]
    CORRECT_PASSWORD = random.choice(PASSWORD_LIST)


@app.route("/")
def index():
    return "Nothing to see here."

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == CORRECT_PASSWORD:
        with open("flag.txt") as f:
            return f.read()
    return "Unauthorized"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
