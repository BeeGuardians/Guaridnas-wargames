from flask import Flask, request
import json  # ✅ 이걸 사용해야 이스케이프 처리가 안전함

app = Flask(__name__)

with open("flag.txt", "r") as f:
    FLAG = f.read()

@app.route("/")
def index():
    q = request.args.get("q", "")
    flag_js = json.dumps(FLAG)  # ✅ 이스케이프된 JS 문자열로 만듦
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>XSS Lab - Easy</title>
        <script>
            var flag = {flag_js};
        </script>
    </head>
    <body>
        <h1>XSS Lab - Easy</h1>
        <div>{q}</div>
        <p>힌트: <code>alert(flag)</code> 를 실행해보세요!</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
