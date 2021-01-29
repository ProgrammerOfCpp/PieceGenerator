from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def route_main():
    return '<a>Hello, world!</a>'


@app.route('/ping')
def route_ping():
    return 'App is running.'


if 'DEBUG' in os.environ:
    app.run()
