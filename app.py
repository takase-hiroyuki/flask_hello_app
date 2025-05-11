from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    return "<h1>こんにちは！Flaskからのメッセージです。</h1>"
