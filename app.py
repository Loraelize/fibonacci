from flask import Flask
from fibonacci import fibonacci

app = Flask(__name__)

# Endpoint que retorna término de la sucesión de Fibonacci indicado en el parámetro.
@app.route("/fibonacci/<int:num>")
def endpoint_fibonacci(num):
    return str(fibonacci(num))
