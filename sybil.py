from flask import Flask
app = Flask(__name__)

print("running")

@app.route('/')
def hello_world():
    return 'Hello World!'