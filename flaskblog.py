"""
A Sample application using python flask framework
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    """
    Home page for the flask app
    """
    return "<h1>Flask Home Page</h1>"


@app.route("/about")
def about():
    """
    About page for the flask app
    """
    return "<h1>Flask About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
