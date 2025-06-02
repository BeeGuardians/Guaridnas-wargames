from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>Steganography Lab</title>
        <style>
            body {
                background-color: #f5f7fa;
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
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 600px;
            }
            h3 {
                color: #2c3e50;
                margin-bottom: 20px;
            }
            img {
                max-width: 100%;
                border: 3px solid #ccc;
                border-radius: 6px;
            }
            p {
                margin-top: 20px;
                font-size: 15px;
                color: #555;
            }
            a.download-btn {
                display: inline-block;
                margin-top: 10px;
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
        </style>
    </head>
    <body>
        <div class="container">
            <h3>🖼️ Steganography Challenge</h3>
            <img src="stego.png" alt="stego image" />
            <p>이 이미지를 우클릭하거나 다운로드 후 분석해 보세요.</p>
            <a href="stego.png" download class="download-btn">👉 이미지 다운로드 (stego.png)</a>
        </div>
    </body>
    </html>
    """

@app.route("/stego.png")
def download():
    return send_file("stego.png", mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
