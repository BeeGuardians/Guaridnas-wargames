from flask import Flask

app = Flask(__name__)

with open("cipher.txt", "r") as f:
    CIPHERTEXT = f.read().strip()

@app.route("/")
def index():
    return f"""
    <html>
    <head><title>Crypto Lab - XOR + Base64</title></head>
    <body>
        <h2>Crypto Lab - XOR + Base64</h2>
        <p>다음 암호문을 복호화하여 FLAG를 찾으세요.</p>
        <pre style="font-size: 1.2em;">{CIPHERTEXT}</pre>
        <hr>
        <p>💡 힌트: Base64 디코딩 후 단일 바이트 키로 XOR 처리됨</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
