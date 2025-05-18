from flask import Flask, request
import sqlite3

app = Flask(__name__)

# DB 초기화
conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users (username TEXT, password TEXT)")
cur.execute("INSERT INTO users VALUES ('admin', 'supersecret')")
conn.commit()

with open("flag.txt", "r") as f:
    FLAG = f.read().strip()

@app.route("/")
def index():
    return '''
        <h1>SQL Injection Lab - Easy</h1>
        <form action="/login" method="GET">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route("/login")
def login():
    username = request.args.get("username", "")
    password = request.args.get("password", "")
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("[DEBUG]", query)
    result = conn.execute(query).fetchone()

    if result:
        return f"<h2>✅ Welcome, {username}!</h2><p>FLAG: {FLAG}</p>"
    else:
        return "<h2>❌ Login failed</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
