from flask_api import FlaskAPI
from flask import Flask, request

"""
Fly API: A Simple, Lightweight API

This is a Flask application that implements
a simple, lightweight API.
"""

app = FlaskAPI(__name__)

@app.route('/example/api/endpoint')
def api_out():
    return {'hello': 'world'}

@app.route('/example/api/receiver', methods=['POST'])
def api_in():
    return {'request data': request.data}

if __name__=="__main__":
    app.run()

