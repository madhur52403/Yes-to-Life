# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 22:41:58 2018

@author: kevin
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import models as dbHandler

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/task')
def task():
    return render_template('task.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


# Getting the login details
@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method=='POST':
   		username = request.form['username']
   		password = request.form['password']
   		dbHandler.insertUser(username, password)

		return redirect(url_for('index'))
   	else:
   		return render_template('login.html')

# Getting the sign up details
@app.route('/signup', methods=['POST', 'GET'])
def signup():
	if request.method=='POST':
   		username = request.form['username']
   		password = request.form['password']
   		dbHandler.insertUser(username, password)

		return redirect(url_for('index'))
   	else:
   		return render_template('signup.html')

       
if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5050)