from main import app
from flask import render_template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")
