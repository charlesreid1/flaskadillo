from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/foo")
def foo():
    return "Hello foo!"

@app.route("/bar/<wuz>")
def bar(wuz):
    return "Hello %s!"%(wuz)


if __name__=="__main__":
    app.run()

