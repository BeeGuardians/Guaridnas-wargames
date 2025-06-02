from flask import Flask, request
import sqlite3

app = Flask(__name__)

# 플래그 로딩
with open("flag.txt", "r") as f:
    FLAG = f.read().strip()

# DB 초기화
conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users (username TEXT, password TEXT)")
cur.execute("INSERT INTO users VALUES (?, ?)", ('admin', FLAG))
conn.commit()


@app.route("/")
def index():
    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>SQL Injection Lab - Easy</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f2f2f2;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .login-container {
                    background-color: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    width: 300px;
                }
                h1 {
                    text-align: center;
                    margin-bottom: 20px;
                    color: #333;
                }
                input[type="text"], input[type="password"] {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input[type="submit"] {
                    width: 100%;
                    padding: 10px;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #45a049;
                }
                .footer {
                    text-align: center;
                    margin-top: 15px;
                    font-size: 12px;
                    color: #888;
                }
            </style>
        </head>
        <body>
            <div class="login-container">
                <h1>Login</h1>
                <form action="/login" method="GET">
                    <label>Username</label>
                    <input type="text" name="username" required>
                    <label>Password</label>
                    <input type="password" name="password" required>
                    <input type="submit" value="Login">
                </form>
                <div class="footer">SQL Injection Lab - Easy</div>
            </div>
        </body>
        </html>
    '''

@app.route("/login")
def login():
    username = request.args.get("username", "")
    password = request.args.get("password", "")
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("[DEBUG]", query)
    result = conn.execute(query).fetchone()

    if result:
        return f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Login Success</title>
                <style>
                    body {{
                        background-color: #e0f7e9;
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }}
                    .message-box {{
                        background-color: white;
                        padding: 30px;
                        border-radius: 10px;
                        box-shadow: 0 0 15px rgba(0, 128, 0, 0.2);
                        text-align: center;
                    }}
                    h2 {{
                        color: #2e7d32;
                        margin-bottom: 10px;
                    }}
                    p {{
                        font-size: 16px;
                        color: #333;
                    }}
                </style>
            </head>
            <body>
                <div class="message-box">
                    <h2>✅ Welcome, {result[0]}!</h2>
                    <p><strong>FLAG:</strong> {result[1]}</p>
                </div>
            </body>
            </html>
        '''
    else:
        return '''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Login Failed</title>
                    <style>
                        body {
                            background-color: #fdecea;
                            font-family: Arial, sans-serif;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                        }
                        .message-box {
                            background-color: white;
                            padding: 30px;
                            border-radius: 10px;
                            box-shadow: 0 0 15px rgba(255, 0, 0, 0.2);
                            text-align: center;
                        }
                        h2 {
                            color: #c62828;
                            margin-bottom: 10px;
                        }
                        a {
                            text-decoration: none;
                            color: #1565c0;
                        }
                    </style>
                </head>
                <body>
                    <div class="message-box">
                        <h2>❌ Login failed</h2>
                        <p>Please <a href="/">try again</a>.</p>
                    </div>
                </body>
                </html>
            '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
