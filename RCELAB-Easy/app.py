from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    host = request.args.get("host", "")
    result = ""
    if host:
        result = os.popen(f"ping -c 1 {host}").read()

    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>RCE Lab - Easy</title>
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
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                width: 600px;
                max-width: 90%;
                text-align: center;
            }}
            h2 {{
                color: #2c3e50;
                margin-bottom: 25px;
            }}
            input[type="text"] {{
                padding: 10px;
                width: 60%;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 15px;
            }}
            input[type="submit"] {{
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 15px;
                margin-left: 10px;
            }}
            input[type="submit"]:hover {{
                background-color: #2980b9;
            }}
            .output {{
                margin-top: 30px;
                text-align: left;
                background-color: #f0f0f0;
                padding: 15px;
                border-radius: 5px;
                font-family: monospace;
                white-space: pre-wrap;
                color: #333;
                max-height: 300px;
                overflow-y: auto;
            }}
            .hint {{
                margin-top: 20px;
                font-size: 14px;
                color: #777;
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>💻 RCE Lab - Easy</h2>
            <form method="GET" action="/">
                <input type="text" name="host" placeholder="예: 8.8.8.8 또는 8.8.8.8 && whoami" required>
                <input type="submit" value="Ping">
            </form>
            <div class="hint">
                <strong>📌 힌트:</strong> 명령어 삽입이 가능한지 테스트해보세요. 예: <code>8.8.8.8 && whoami</code>
            </div>
            {'<div class="output">' + result + '</div>' if result else ''}
        </div>
    </body>
    </html>
    '''


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    result = os.popen(f"ping -c 1 {host}").read()
    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
