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

## how to use this directory

create a virtual environment, which we'll call `vp` (you can use any name you want):

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

