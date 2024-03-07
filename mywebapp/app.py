from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return {
        "mesage": "Hello Wold",
         "status": 200   
            }


app.run(port=5000)