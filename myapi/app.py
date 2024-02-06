from flask import Flask, jsonify, request, json

app = Flask(__name__)

cars = [
    {
    "car1": "Ford",
    "car2": "Ferrari"
    },
    {
    "car3": "Ford3",
    "car4": "Ferrari3"
    }
    ]

@app.route('/')
def say_hello():
    return jsonify({"message": "Welcome to my applicaiton"})


@app.route('/new', methods=['GET'])
def list_cars():
    return jsonify(cars)

@app.route('/new/<car: str>', methods=['GET'])
def list_cars(car: str):
    return jsonify(cars['car'])


@app.route('/new', methods=['POST'])
def update_cars():
    print(request)
    data = request.json
    cars.append(data)
    response_data = json.dumps({'status': 'posted successfully'})

    return jsonify(response_data)


app.run(debug=True)

