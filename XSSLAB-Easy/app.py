from flask import Flask, request
import json  # ✅ 이걸 사용해야 이스케이프 처리가 안전함

app = Flask(__name__)

with open("flag.txt", "r") as f:
    FLAG = f.read()

@app.route("/")
def index():
    q = request.args.get("q", "")
    flag_js = json.dumps(FLAG)  # 안전한 JS 문자열 생성

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>XSS Lab - Easy</title>
        <style>
            body {{
                background-color: #f4f6f8;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .lab-container {{
                background-color: #fff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                width: 600px;
                text-align: center;
            }}
            h1 {{
                color: #2c3e50;
                margin-bottom: 20px;
            }}
            form {{
                margin-bottom: 20px;
            }}
            input[type="text"] {{
                width: 70%;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin-right: 10px;
            }}
            input[type="submit"] {{
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            input[type="submit"]:hover {{
                background-color: #2980b9;
            }}
            .output {{
                margin-top: 20px;
                padding: 15px;
                background-color: #ecf0f1;
                border-radius: 5px;
                word-break: break-word;
                color: #2c3e50;
            }}
            .hint {{
                margin-top: 10px;
                font-size: 14px;
                color: #888;
            }}
        </style>
        <script>
            var flag = {flag_js};
        </script>
    </head>
    <body>
        <div class="lab-container">
            <h1>XSS Lab - Easy</h1>
            <form method="GET" action="/">
                <input type="text" name="q" placeholder="여기에 입력해 보세요" required>
                <input type="submit" value="검색">
            </form>
            <div class="output">{q}</div>
            <div class="hint">💡 힌트: <code>alert(flag)</code> 를 실행해보세요!</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
