from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/book")
def book():
    return render_template('book.html')

                



