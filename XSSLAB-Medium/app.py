from flask import Flask, request, jsonify

app = Flask(__name__)

with open("flag.txt", "r") as f:
    FLAG = f.read()

@app.route("/")
def index():
    q = request.args.get("q", "")
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>XSS Lab - Medium</title>
    </head>
    <body>
        <h1>XSS Lab - Medium</h1>
        <h2>👋 Hello {q}</h2>
        <p>이 페이지는 검색어를 필터링 없이 그대로 출력합니다.</p>

        <div>
            <strong>힌트 🕵️‍♂️</strong><br>
            - 검색어는 HTML에 그대로 삽입됩니다.<br>
            - 자바스크립트로 <code>/flag</code> 엔드포인트에 <code>fetch()</code> 요청을 보내보세요.<br>
            - 응답으로 받은 JSON 객체에서 <code>flag</code> 값을 꺼내 <code>alert()</code>로 출력해보세요.<br>
        </div>
    </body>
    </html>
    """

@app.route("/flag")
def get_flag():
    return jsonify({"flag": FLAG})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
