import flask
from flask import Flask, request, flash
# from flask_sqlalchemy import SQLAlchemy

# import os
# import jinja_partials
app = Flask(__name__)
app.config.from_object("config")
# db = SQLAlchemy(app)


# jinja_partials.register_extensions(app)

# from . import views,models

@app.route("/")
def index(): 
    return flask.render_template('index.html')

@app.route("/css")
def css(): 
    return flask.render_template('style.css')

@app.route("/about/")
def about():
    return ("<h1>about</h1>")

@app.route('/SomeFunction/getQuery')
def getQueryt(str):
    print("я хабрал запрос")
    return "держи свое проанализированное гавно"

@app.route("/query")
def query():
    
        if request.method == "GET":
            if len(request.form['query_text']>2):
                flash('Ваш ответ генерируется, подождите, пожалуйста')
                print (request.form['query_text'])
            return
        return

        