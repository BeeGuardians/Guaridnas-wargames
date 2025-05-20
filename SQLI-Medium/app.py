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
    return "<h2>Try accessing /profile?id=1</h2>"

@app.route("/profile")
def profile():
    user_id = request.args.get("id", "")
    query = f"SELECT username FROM users WHERE id = {user_id}"
    print("[DEBUG]", query)
    try:
        result = conn.execute(query).fetchone()
        if result and result[0]:
            return f"<h3>Username: {result[0]}</h3>"
        else:
            return "<h3>No such user or username is empty.</h3>"
    except Exception as e:
        return f"<h3>Invalid input</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
