from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h3>스테가노 이미지:</h3>
    <img src="/stego.png" alt="stego image" style="max-width: 400px; border: 2px solid #ccc;" />
    <p>이미지를 우클릭하거나 저장해 분석해보세요.</p>
    """

@app.route("/stego.png")
def download():
    return send_file("stego.png", mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
