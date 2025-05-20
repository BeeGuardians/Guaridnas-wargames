from flask import Flask, request, make_response

app = Flask(__name__)

FLAG = "FLAG{xss_cookie_steal_success}"

@app.route("/")
def index():
    q = request.args.get("q", "")
    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>XSS Lab - Cookie Stealer</title></head>
    <body>
        <h2>XSS Lab - Cookie Stealer</h2>
        <p>검색어: {q}</p>
    </body>
    </html>
    """
    resp = make_response(html)
    resp.set_cookie("FLAG", FLAG)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
