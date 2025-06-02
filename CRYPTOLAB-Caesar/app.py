from flask import Flask

app = Flask(__name__)

ciphertext = "IURG{fdhvdu_flskhu_lv_ixq}"

@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Crypto Lab - Caesar Cipher</title>
        <style>
            body {{
                background-color: #f5f7fa;
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
                width: 650px;
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
                font-size: 1.3em;
                font-weight: bold;
                color: #2c3e50;
                word-break: break-all;
                white-space: pre-wrap;
            }}
            .hint {{
                background-color: #eef3f9;
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
            <h2>🔐 Crypto Lab - Caesar Cipher</h2>
            <p>다음 암호문을 복호화해서 <strong>FLAG</strong>를 찾아보세요.</p>
            <pre class="cipher">{ciphertext}</pre>
            <div class="hint">
                💡 <strong>힌트:</strong> Caesar Cipher는 각 알파벳을 일정 수만큼 밀어 암호화합니다.<br>
                예: A → D, B → E (시프트 +3)
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
