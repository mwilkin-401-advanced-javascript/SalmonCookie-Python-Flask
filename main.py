from settings import NAME
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", name=NAME)

@app.route('/sales')
def sales_route():
    return render_template("sales.html", name=NAME)

@app.route('/info')
def info_route():
    return render_template("info.html", name=NAME)

@app.route('/about')
def about_route():
    return render_template("about.html", name=NAME)

@app.route('/merch')
def merch_route():
    return render_template("merch.html", name=NAME)