from cmath import sqrt
from operator import methodcaller
import re
from flask import Flask, render_template, request, redirect, url_for, flash
import math


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/square', methods=['POST', 'GET'])
def square():
    error = ''
    if request.method == 'POST':
        x = int(request.form['number'])
        y = math.sqrt(x)
        return render_template('answer.html', y=y)
        
    return render_template('square.html')

@app.route('/hypotenusa', methods=['POST','GET'])
def hypotenusa():
    if request.method == 'POST':
        x = request.form['leg1']
        y = request.form['leg2']
        code = math.hypot(int(x),int(y))
        return render_template('answer.html', code=code)
    return render_template('hypotenusa.html')

@app.route('/convert', methods=['POST', 'GET'])
def convert():
    convert = ''
    if request.method == 'POST':
        grade = request.form['grade']
        grade = int(grade)
        if grade >= 0 and grade < 65:
            convert = "Grade E"
        elif grade >= 65 and grade <= 66:
            convert = "Grade D"
        elif grade >= 67 and grade <= 69:
            convert = "Grade D+"
        elif grade >= 70 and grade <= 72:
            convert = "Grade C-"
        elif grade >= 73 and grade <= 76:
            convert = "Grade C"
        elif grade >= 77 and grade <= 79:
            convert = "Grade C+"
        elif grade >= 80 and grade <= 82:
            convert = "Grade B-"
        elif grade >= 83 and grade <= 86:
            convert = "Grade B"
        elif grade >= 87 and grade <= 89:
            convert = "Grade B+"
        elif grade >= 90 and grade <= 92:
            convert = "Grade A-"
        elif grade >= 93 and grade <= 96:
            convert = "Grade A"
        elif grade >= 97 and grade <= 100:
            convert = "Grade A+"
        return render_template('answer.html', convert=convert)
        
    return render_template('convert.html')



       
        
        

