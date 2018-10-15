from flask import Flask, render_template

"""
Flask Example with Jinja Templates

This is a simple Flask server example
with a template HTML page.
"""

app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template(
            'main.html',
            name="Florence",
            list_items=['peanut butter','jelly','bananas','bread']
    )

if __name__ == '__main__':
    app.run(port=5000)

