from flask import Flask, render_template
import os
from os.path import abspath, join, dirname

base = os.path.split(os.path.abspath(__file__))[0]

app = Flask(
        __name__,
        template_folder = os.path.join(base,'templates'),
        static_folder = os.path.join(base,'static')
)

@app.route('/')
def index():
    return "Hello world"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

