from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
number = 1
def hello_world():
    return number
