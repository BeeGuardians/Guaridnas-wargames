from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <h2>RCE Lab - Easy</h2>
        <form action="/ping" method="GET">
            Host: <input name="host">
            <input type="submit" value="Ping">
        </form>
    '''

@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    result = os.popen(f"ping -c 1 {host}").read()
    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
