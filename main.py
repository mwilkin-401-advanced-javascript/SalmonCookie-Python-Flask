from settings import NAME
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # return f"Hello, { NAME }"
    return render_template("home.html", name=NAME)

@app.route('/sales')
def second_route():
    return render_template("sales.html", name=NAME)