from flask import Flask

app = Flask(__name__)

with open("cipher.txt", "r") as f:
    CIPHERTEXT = f.read().strip()

@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Crypto Lab - XOR + Base64</title>
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
                background-color: #ffffff;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
                width: 700px;
                max-width: 90%;
                text-align: center;
            }}
            h2 {{
                color: #2c3e50;
                margin-bottom: 20px;
            }}
            pre.cipher {{
                background-color: #f0f0f0;
                padding: 20px;
                border-radius: 8px;
                font-size: 1.2em;
                word-break: break-all;
                text-align: left;
                overflow-x: auto;
                white-space: pre-wrap;
            }}
            .hint {{
                background-color: #eaf2f8;
                padding: 15px;
                border-left: 5px solid #3498db;
                color: #2c3e50;
                margin-top: 30px;
                border-radius: 5px;
                font-size: 15px;
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🔐 Crypto Lab - XOR + Base64</h2>
            <p>다음 암호문을 복호화하여 <strong>FLAG</strong>를 찾으세요.</p>
            <pre class="cipher">{CIPHERTEXT}</pre>
            <div class="hint">
                💡 <strong>힌트:</strong> Base64 디코딩 후 단일 바이트 키로 XOR 처리된 문자열입니다.<br>
                예: <code>for b in data: b ^ key</code>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
