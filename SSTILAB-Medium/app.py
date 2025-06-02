from flask import Flask, request, render_template_string

app = Flask(__name__)

with open("flag.txt", "r") as f:
    FLAG = f.read()

@app.route("/")
def index():
    name = request.args.get("name", "guest")
    template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>SSTI Lab</title>
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
            .container {{
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0,0,0,0.1);
                width: 600px;
                text-align: center;
            }}
            h1 {{
                color: #2c3e50;
            }}
            form {{
                margin-top: 20px;
            }}
            input[type="text"] {{
                padding: 10px;
                width: 70%;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            input[type="submit"] {{
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                margin-left: 10px;
                cursor: pointer;
            }}
            .hint {{
                margin-top: 20px;
                text-align: left;
                background-color: #f0f3f4;
                padding: 15px;
                border-radius: 8px;
                font-size: 14px;
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
            <h1>SSTI Lab - Easy</h1>
            <form method="GET" action="/">
                <input type="text" name="name" placeholder="이름을 입력하거나 SSTI 테스트" required>
                <input type="submit" value="확인">
            </form>
            <div style="margin-top: 30px;">
                <h2>Hello {name}</h2>
            </div>
            <div class="hint">
                <strong>🧪 힌트:</strong><br>
                - 이 앱은 <code>render_template_string</code>을 사용하여 사용자 입력을 템플릿에 직접 삽입합니다.<br>
                - 예: <code>{{ "{{7*7}}" }}</code> 와 같은 입력을 시도해보세요.<br>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(template)

@app.route("/source")
def source():
    return "<pre>" + open(__file__).read() + "</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
