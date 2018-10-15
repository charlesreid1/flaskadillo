# hello: flask hello world

Flask home page: <http://flask.pocoo.org/>

## the simplest flask app

Here is the simplest Flask app:

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

This directory contains files to get this server up and running.

# hello: quick start

## how to set up this directory

Create a virtual environment, which we'll call `vp` (you can use any name you want):

```
virtualenv vp
```

This creates a "clean" version of `python` and `pip` that are separate from your 
normal version of Python and pip.

To install Flask into this virtual environment:

```
pip install -r requirements.txt
```

The `requirements.txt` file just contains the name of any Python packages
that should be installed, and optional version numbers. In this case, we
only install Flask, so the contents of `requirements.txt` is:

```
Flask>=1.0
``` 

## how to run the web app

The Flask web application is stored in the variable `app` (see `simple.py`).

To run the Flask app, you call `app.run()`.


## how to test the web app

To test the simple Flask web app, you can use the Python `unittest` module from
the command line:

```
python -m unittest discover
```

This will find and run the Flask test.

To run a Flask test, you only need to create the test client - the server is taken
care of for you.

```
client = app.test_client()
```

This is a built-in Flask method that returns a client object.

The client object can run get and post methods on URLs.
The simple server only needs get methods to test routes:

```
# Test route /
r = client.get('/')
assert b'Hello world!' in r.data
```



