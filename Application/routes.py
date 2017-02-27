#!/usr/bin/python
#-*- coding:utf-8 -*-
from flask import Flask, url_for
from flask import render_template, flash, redirect, session, request, g, jsonify
app = Flask(__name__)

def f(x):
	return x+5


@app.route('/')
def home():
    with open('/home/runique/FirstWebStudy/Application/views.txt','r') as fp:
        a = int(fp.read())
    a = a + 1
    
    with open('/home/runique/FirstWebStudy/Application/views.txt','w') as fp:
        fp.write(str(a))
    return render_template('index.html',number=a)


@app.route('/ryun')
def ryun():
    return render_template('ryun.html')

@app.route('/ryun/<int:number>')
def ryun_detail(number):
	print number
	return render_template('ryun_detail.html',number=number)


if __name__ == '__main__':
    app.run(host='14.63.88.216',port=5998,debug=True,threaded=True)

