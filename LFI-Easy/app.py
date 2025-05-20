from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    page = request.args.get("page", "home")
    try:
        with open(f"pages/{page}", "r") as f:
            return f.read()
    except Exception:
        return "<h2>Page not found</h2>", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
