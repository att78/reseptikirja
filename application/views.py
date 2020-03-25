from flask import render_template
from application import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/main")
def main():
    
    return render_template("main.html")


