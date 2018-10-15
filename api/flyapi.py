from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/example/api/endpoint')
def api_out():
    return {'hello': 'world'}

@app.route('/example/api/receiver')
def api_in():
    return {'request data': request.data}




