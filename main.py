#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> hello, world!</h1>"


@app.route("/info")
def hello_test():
    return "<h1>This is some info.</h1>"



@app.route("/api/helloworld")
def me_api():
    return {
        "date":"some date",
        "title":"helloworld",
        "msg":"helloworld",
    }





