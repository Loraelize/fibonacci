from flask import Flask

app = Flask(__name__)

@app.route("/fibonacci")
def hello_world():
    return "<p>Hello, World!</p>"
