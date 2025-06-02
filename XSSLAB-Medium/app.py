from flask import Flask, request, jsonify

app = Flask(__name__)

with open("flag.txt", "r") as f:
    FLAG = f.read()

@app.route("/")
def index():
    q = request.args.get("q", "")

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>XSS Lab - Medium</title>
        <style>
            body {{
                background-color: #f9f9f9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .container {{
                background-color: #fff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
                width: 600px;
                text-align: center;
            }}
            h1 {{
                color: #2c3e50;
                margin-bottom: 10px;
            }}
            h2 {{
                color: #34495e;
                margin: 20px 0;
            }}
            form {{
                margin-bottom: 20px;
            }}
            input[type="text"] {{
                padding: 10px;
                width: 75%;
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
            .hint {{
                margin-top: 25px;
                background-color: #f0f3f4;
                padding: 15px;
                border-radius: 8px;
                font-size: 14px;
                text-align: left;
                color: #555;
            }}
            code {{
                background-color: #eee;
                padding: 2px 5px;
                border-radius: 3px;
                font-family: monospace;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>XSS Lab - Medium</h1>
            <form method="GET" action="/">
                <input type="text" name="q" placeholder="이름 또는 스크립트를 입력하세요" required>
                <input type="submit" value="확인">
            </form>

            <h2>👋 Hello {q}</h2>
            <p>이 페이지는 검색어를 필터링 없이 그대로 출력합니다.</p>

            <div class="hint">
                <strong>🔍 힌트</strong><br>
                - 검색어는 <b>HTML에 그대로 삽입</b>됩니다.<br>
                - JavaScript로 <code>/flag</code> 엔드포인트에 <code>fetch()</code> 요청을 보내보세요.<br>
                - 응답으로 받은 JSON 객체에서 <code>flag</code> 값을 꺼내 <code>alert()</code>로 출력해보세요.<br><br>
                예시:
                <pre><code>fetch('/flag')
  .then(res => res.json())
  .then(data => alert(data.flag))</code></pre>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/flag")
def get_flag():
    return jsonify({"flag": FLAG})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
