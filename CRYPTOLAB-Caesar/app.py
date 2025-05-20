from flask import Flask

app = Flask(__name__)

ciphertext = "IURG{fdhvdu_flskhu_lv_ixq}"

@app.route("/")
def index():
    return f"""
    <html>
    <head><title>Crypto Lab - Caesar Cipher</title></head>
    <body>
        <h2>Crypto Lab - Caesar Cipher</h2>
        <p>다음 암호문을 복호화해서 FLAG를 찾아보세요.</p>
        <pre style="font-size: 1.2em;">{ciphertext}</pre>
        <hr>
        <p>💡 Caesar Cipher는 알파벳을 일정 수만큼 밀어 암호화합니다.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
