from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Wththorld!</p>"

@app.route("/louise")
def louise():
    return "<p>Hello, louise!</p>"

@app.route("/alyssa")
def alyssa():
    return "<p>Hello, alyssa!</p>"

@app.route("/name/<my_name>")
def name(my_name):
    for i in request.args:
        print(i)
    age= request.args.get("age")
    weight= request.args.get("weight")
    return f"<p>{my_name} is {age} yo and weighs {weight} !</p>"