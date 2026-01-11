from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# ★ ここが新しい
@app.route("/save", methods=["POST"])
def save():
    data = request.json
    print("受け取ったデータ👇")
    print(data)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
