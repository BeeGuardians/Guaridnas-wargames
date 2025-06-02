from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    page = request.args.get("page", "home")
    status = 200
    try:
        with open(f"pages/{page}", "r") as f:
            result = f.read()
    except Exception:
        result = "<h3>❌ Page not found</h3>"
        status = 404

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>LFI Lab - Easy</title>
        <style>
            body {{
                background-color: #f5f7fa;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }}
            .container {{
                background-color: #fff;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
                width: 700px;
                max-width: 90%;
            }}
            h2 {{
                color: #2c3e50;
                margin-bottom: 20px;
                text-align: center;
            }}
            form {{
                text-align: center;
                margin-bottom: 20px;
            }}
            input[type="text"] {{
                padding: 10px;
                width: 60%;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
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
            input[type="submit"]:hover {{
                background-color: #2980b9;
            }}
            .output {{
                background-color: #f0f0f0;
                padding: 20px;
                border-radius: 8px;
                white-space: pre-wrap;
                font-family: monospace;
                color: #333;
                max-height: 400px;
                overflow-y: auto;
            }}
            .hint {{
                margin-top: 20px;
                font-size: 14px;
                color: #555;
                background-color: #eef3f7;
                padding: 10px;
                border-radius: 5px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>📄 LFI Lab - Easy</h2>
            <form method="get" action="/">
                <input type="text" name="page" placeholder="예: home or ../../etc/passwd" value="{page}" required>
                <input type="submit" value="Load">
            </form>
            <div class="output">{result}</div>
            <div class="hint">
                <strong>💡 힌트:</strong> <code>?page=home.html</code> 또는 <code>?page=../../../../etc/passwd</code> 를 시도해보세요.
                <br>파일 시스템을 탐색할 수 있을지도 몰라요!
            </div>
        </div>
    </body>
    </html>
    """, status


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
