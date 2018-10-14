# the simplest flask package

This is the simplest imaginable flask package
that comes bundled with a built-in webapp.

## Quick Start

Start by installing the `simple` package:

```
python setup.py build install
```

Now you can import it and use the `webapp` submodule's
`app` variable to run the Flask app. From a Python
interactive prompt,

```
>>> import simple
>>> app = simple.webapp.app
>>> app.run(port=5001)
```

Now visit <http://localhost:5001> to see the hello world message,
or <http://localhost:5001/hello/borg> to see a Hello Borg message.

