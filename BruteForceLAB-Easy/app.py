from flask import Flask, request
import random

app = Flask(__name__)

# 랜덤 비밀번호 선택
with open("passwords.txt") as f:
    PASSWORD_LIST = [line.strip() for line in f.readlines()]
    CORRECT_PASSWORD = random.choice(PASSWORD_LIST)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Brute Force Lab - Login</title>
        <style>
            body {
                background-color: #f4f6f8;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .login-container {
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                width: 400px;
                text-align: center;
            }
            h2 {
                color: #2c3e50;
                margin-bottom: 20px;
            }
            input[type="text"], input[type="password"] {
                width: 80%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 14px;
            }
            input[type="submit"]:hover {
                background-color: #2980b9;
            }
            .hint {
                margin-top: 20px;
                font-size: 14px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <h2>🔐 Brute Force Lab</h2>
            <form method="POST" action="/login">
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <input type="submit" value="Login">
            </form>
            <div class="hint">
                💡 <strong>힌트:</strong> 비밀번호는 <code>passwords.txt</code> 중 하나입니다.
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "admin" and password == CORRECT_PASSWORD:
        with open("flag.txt") as f:
            return f"<pre>{f.read()}</pre>"
    return """
    <html><body style='text-align:center;font-family:sans-serif;padding-top:50px;'>
    <h3>❌ Unauthorized</h3>
    <a href="/">🔙 Try again</a>
    </body></html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
