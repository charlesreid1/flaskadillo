# hello: flask hello world

Flask home page: <http://flask.pocoo.org/>

Here is the simplest Flask app:

```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

