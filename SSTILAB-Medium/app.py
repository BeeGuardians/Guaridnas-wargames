from flask import Flask, request, render_template_string

app = Flask(__name__)

FLAG = "FLAG{ssti_execution_success}"

@app.route("/")
def index():
    name = request.args.get("name", "guest")
    template = f"<h2>Hello {name}</h2>"
    return render_template_string(template)

@app.route("/source")
def source():
    return "<pre>" + open(__file__).read() + "</pre>"

@app.route("/flag")
def flag():
    return FLAG  # 실제 문제에서는 숨기거나 / 내부에서만 호출되도록 수정 가능

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
