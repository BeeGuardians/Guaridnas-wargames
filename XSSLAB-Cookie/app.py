from flask import Flask, request, make_response

app = Flask(__name__)

with open("flag.txt", "r") as f:
    FLAG = f.read()

@app.route("/")
def index():
    q = request.args.get("q", "")
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>XSS Lab - Cookie Stealer</title>
        <style>
            body {{
                background-color: #f0f2f5;
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
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                width: 500px;
                text-align: center;
            }}
            h2 {{
                color: #2c3e50;
                margin-bottom: 20px;
            }}
            form {{
                margin-bottom: 20px;
            }}
            input[type="text"] {{
                padding: 10px;
                width: 80%;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin-bottom: 10px;
            }}
            input[type="submit"] {{
                padding: 10px 20px;
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            input[type="submit"]:hover {{
                background-color: #2980b9;
            }}
            .result {{
                margin-top: 20px;
                padding: 15px;
                background-color: #ecf0f1;
                border-radius: 5px;
                word-wrap: break-word;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>XSS Lab - Cookie Stealer</h2>
            <form method="GET" action="/">
                <input type="text" name="q" placeholder="검색어를 입력하세요" required>
                <br>
                <input type="submit" value="검색">
            </form>
            <div class="result">
                검색어: {q}
            </div>
        </div>
    </body>
    </html>
    """
    resp = make_response(html)
    resp.set_cookie("FLAG", FLAG)
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
