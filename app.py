""" add_me: add template inheritance and multiple routes
 			also add a form if possible // learn sessions and then use that too
  			make something // use css also
			add a password hashing method to hash the password, when logging in, hash the input
			password and match

"""
# THIS PROGRAM RUNS
# THIS PROGRAM RUNS
# THIS PROGRAM RUNS
# THIS PROGRAM RUNS


from flask import Flask, render_template, request
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql+psycopg2://postgres:Nru$ingh@localhost:5432/project1")
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres@localhost/postgres"
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reg")
def reg():
	# greet=name+" "+"Welcome to the first Flask app"
	return render_template("reg.html")

@app.route("/success", methods=["GET","POST"])
def succ():
	usrnm = request.form.get("usernm")
	pswd = request.form.get("pass")
	query="insert into data (username,passwords) values ('" + usrnm+ "','" + pswd + "');"
	# if engine.execute("INSERT INTO data (username,passwords) values (:usrnm, :pswd)",{ "usrnm": usrnm,"pswd": pswd}):
		# engine.execute("INSERT INTO data (username,passwords) values (:usrnm, :pswd);",{ 'usrnm': usrnm,'pswd': pswd})
		# engine.execute(query)
		# print (usrnm, pswd)
		# succ(usrnm, pswd)
	if engine.execute(query):

		return render_template("succ.html", user=usrnm, passs=pswd)
	else:
		return render_template(error.html)

@app.route("/login")
def login():
	return render_template("login.html")

# @app.route("/success")
# def succ(user, passs):
# 	# return render_template(suc.html, passs=passs, user=user)
# 	pass