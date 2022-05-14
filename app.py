from flask import Flask

app = Flask(__name__)

@app.route("/fibonacci/<int:num>")
def endpoint_fibonacci(num):
    return str(num)
