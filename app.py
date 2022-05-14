from flask import Flask

app = Flask(__name__)


@app.route("/fibonacci/<int:num>")
def endpoint_fibonacci(num):
    return str(fibonacci(num))


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
