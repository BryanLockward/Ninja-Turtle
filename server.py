from flask import Flask, render_template, request, session, flash, redirect
app = Flask(__name__)
app.secret_key = "secretKey"
import types

@app.route('/')
def index():
    msg="No Ninjas Here"
    flash(msg)
    return render_template("index.html")

@app.route('/ninja')
def display_all():
    msg='all'

    flash(msg)
    return render_template("index.html")

@app.route("/ninja/<turtle>")
def display_one(turtle):
    msg=turtle
    flash(msg)

    return render_template("index.html")




app.run(debug=True)
