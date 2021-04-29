# Put your app in here.
from flask import Flask, request
from operator import add, sub, mul, truediv

app = Flask(__name__)


@app.route("/add")
def do_add():
    """Add a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = add(a, b)
    return str(result)


@app.route("/sub")
def do_sub():
    """Substract b from a."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = sub(a, b)
    return str(result)


@app.route("/mult")
def do_mult():
    """Multiply a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = mul(a, b)
    return str(result)


@app.route("/div")
def do_div():
    """Divide a by b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = truediv(a, b)
    return str(result)


operations = {"add": add, "sub": sub, "mult": mul, "div": truediv}


@app.route("/math/<operator>")
def do_math(operator):

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = operations[operator](a, b)
    return str(result)
