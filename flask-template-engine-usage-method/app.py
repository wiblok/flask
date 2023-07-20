from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    message = "hello world"
    return render_template("hello.html", message=message)

