from flask import Flask, request, redirect
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<menu>")
def menu(menu):
    return render_template(menu)

@app.route("/<about>")
def about(about):
    return render_template(about)

@app.route("/<book>")
def book(book):
    return render_template(book)

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    return 'Got it!'


