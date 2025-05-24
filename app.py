from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    return "<h1>こんばんは！　takaseからのメッセージです。</h1>"

# 🔻 Renderで必要な起動コードを追加
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

