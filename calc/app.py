# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route("/add")
def add_two_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.add(a, b))

@app.route("/subtract")
def sub_two_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.sub(a, b))

@app.route("/multiply")
def mult_two_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.mult(a, b))

@app.route("/divide")
def div_two_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.div(a, b))