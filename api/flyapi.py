from flask_api import FlaskAPI

"""
Fly API: A Simple, Lightweight API

This is a Flask application that implements
a simple, lightweight API.
"""

app = FlaskAPI(__name__)

@app.route('/example/api/endpoint')
def api_out():
    return {'hello': 'world'}

@app.route('/example/api/receiver')
def api_in():
    return {'request data': request.data}

