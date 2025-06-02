from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Crypto Lab - Weak RSA Key</title>
        <style>
            body {
                background-color: #f4f6f8;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background-color: #ffffff;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                width: 650px;
                max-width: 90%;
            }
            h2 {
                color: #2c3e50;
                margin-bottom: 15px;
            }
            p {
                font-size: 15px;
                color: #555;
                line-height: 1.6;
            }
            ul {
                list-style-type: none;
                padding-left: 0;
                margin-top: 20px;
            }
            li {
                margin-bottom: 10px;
            }
            a.download-btn {
                display: inline-block;
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            a.download-btn:hover {
                background-color: #2980b9;
            }
            .box {
                background-color: #f9f9f9;
                padding: 15px;
                border-left: 5px solid #3498db;
                margin-top: 30px;
                border-radius: 5px;
            }
            code {
                background-color: #eee;
                padding: 2px 6px;
                border-radius: 4px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🔐 Crypto Lab - Weak RSA Key</h2>
            <p>이 서버는 RSA 공개키로 암호화된 메시지를 제공합니다.</p>
            <p><strong>공개키의 n 값이 작고, e = 3</strong>으로 설정되어 있어, <br>
            <strong>Wiener's Attack</strong> 또는 <strong>작은 메시지 공격</strong>이 가능한 환경입니다.</p>

            <p>아래 파일을 다운로드하여 복호화에 도전해보세요:</p>
            <ul>
                <li><a class="download-btn" href="/public.pem" download>📄 공개키 받기 (public.pem)</a></li>
                <li><a class="download-btn" href="/ciphertext.txt" download>🧾 암호문 받기 (ciphertext.txt)</a></li>
            </ul>

            <div class="box">
                <p><strong>📌 목표:</strong> 암호문을 복호화하여 <code>FLAG{{...}}</code> 형식의 플래그를 얻으세요.</p>
                <p><strong>💡 힌트:</strong> <code>RsaCtfTool</code>, <code>SageMath</code>, 또는 직접 수식 복원 모두 가능합니다.</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/public.pem")
def public_key():
    return send_file("public.pem", mimetype="application/x-pem-file")

@app.route("/ciphertext.txt")
def ciphertext():
    return send_file("ciphertext.txt", mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
