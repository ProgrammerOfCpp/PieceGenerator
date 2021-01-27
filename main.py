from flask import Flask

app = Flask(__name__)


@app.route('/')
def route_main():
    return '<a>Hello, world!</a>'


