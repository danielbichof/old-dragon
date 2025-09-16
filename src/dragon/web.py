from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("home.html")


def run():
    app.run(host="127.0.0.1", port=8000, debug=True)
