from flask import Flask, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()

# 플래그 로딩
with open("flag.txt", "r") as f:
    FLAG = f.read().strip()

# DB 초기화
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT, flag TEXT)")
cur.executemany("INSERT INTO users (id, username, email, flag) VALUES (?, ?, ?, ?)", [
    (1, 'alice', 'alice@example.com', ''),
    (2, 'bob', 'bob@example.com', ''),
    (3, 'carol', 'carol@example.com', ''),
    (4, 'dave', 'dave@example.com', ''),
    (5, '', '', FLAG),
])
conn.commit()

@app.route("/")
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>SQLi Lab - Profile Lookup</title>
        <style>
            body {
                background-color: #f8f9fa;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #fff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
                text-align: center;
                width: 500px;
            }
            h2 {
                color: #333;
            }
            input[type="text"] {
                padding: 10px;
                width: 60%;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                margin-left: 10px;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
            .hint {
                margin-top: 25px;
                font-size: 14px;
                color: #666;
                background-color: #f1f1f1;
                padding: 10px;
                border-radius: 6px;
                text-align: left;
            }
            code {
                background-color: #eee;
                padding: 2px 4px;
                border-radius: 3px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🔍 SQL Injection Lab - Profile Lookup</h2>
            <form action="/profile" method="get">
                <input type="text" name="id" placeholder="Enter user id (e.g., 1)" required>
                <input type="submit" value="조회">
            </form>
            <div class="hint">
                <strong>💡 힌트</strong><br>
                - URL 또는 입력창에 <code>?id=1</code>, <code>?id=5</code> 등의 값 입력<br>
                - 예: <code>?id=1 UNION SELECT flag FROM users WHERE id=5</code><br>
                - SQL Injection 실습을 위해 파라미터 필터링이 없습니다.
            </div>
        </div>
    </body>
    </html>
    '''


@app.route("/profile")
def profile():
    user_id = request.args.get("id", "")
    query = f"SELECT username FROM users WHERE id = {user_id}"
    print("[DEBUG]", query)
    try:
        result = conn.execute(query).fetchone()
        if result and result[0]:
            return f'''
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Profile Result</title>
                    <style>
                        body {{
                            background-color: #eafaf1;
                            font-family: Arial, sans-serif;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                        }}
                        .result {{
                            background-color: white;
                            padding: 30px;
                            border-radius: 10px;
                            box-shadow: 0 0 10px rgba(0, 128, 0, 0.2);
                            text-align: center;
                        }}
                        h3 {{
                            color: #2e7d32;
                        }}
                        a {{
                            display: inline-block;
                            margin-top: 20px;
                            text-decoration: none;
                            color: #007bff;
                        }}
                    </style>
                </head>
                <body>
                    <div class="result">
                        <h3>👤 Username: {result[0]}</h3>
                        <a href="/">🔙 Back</a>
                    </div>
                </body>
                </html>
            '''
        else:
            return '''
                <!DOCTYPE html>
                <html>
                <head><title>No User</title></head>
                <body style="text-align:center;font-family:sans-serif;padding-top:50px;">
                    <h3>🚫 No such user or username is empty.</h3>
                    <a href="/">🔙 Back</a>
                </body>
                </html>
            '''
    except Exception as e:
        return '''
            <!DOCTYPE html>
            <html>
            <head><title>Invalid Input</title></head>
            <body style="text-align:center;font-family:sans-serif;padding-top:50px;">
                <h3>⚠️ Invalid input</h3>
                <p style="color:gray;">쿼리 오류 또는 SQL Injection 구문 오류입니다.</p>
                <a href="/">🔙 Back</a>
            </body>
            </html>
        '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
