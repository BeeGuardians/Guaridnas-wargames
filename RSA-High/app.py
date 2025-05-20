from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
    <head><title>Crypto Lab - Weak RSA Key</title></head>
    <body>
        <h2>🔐 Crypto Lab - Weak RSA Key</h2>
        <p>이 서버는 RSA 공개키로 암호화된 메시지를 제공합니다.</p>
        <p>공개키의 n 값이 매우 작고, e = 3으로 설정되어 있습니다.</p>
        <p>이로 인해 <strong>개인키 복원 공격(Wiener's Attack 또는 작은 메시지 공격)</strong>이 가능합니다.</p>

        <p>아래 파일을 다운로드하여 복호화에 도전하세요:</p>
        <ul>
            <li><a href="/public.pem" download>📄 공개키 (public.pem)</a></li>
            <li><a href="/ciphertext.txt" download>🧾 암호문 (ciphertext.txt)</a></li>
        </ul>

        <hr>
        <p>📌 목표: 암호문을 복호화하여 <code>FLAG{...}</code> 형식의 플래그를 얻으세요.</p>
        <p>💡 힌트: RsaCtfTool, SageMath, 손수 복원 모두 가능합니다.</p>
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
