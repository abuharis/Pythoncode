from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return {
        "message": "hai"
    }


app.run()