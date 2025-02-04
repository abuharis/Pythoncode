""""
A REST API (Representational State Transfer) is an architectural style for creating web services. 
It uses standard HTTP methods to perform CRUD (Create, Read, Update, Delete) operations.

HTTP Methods:

GET: Retrieve data from the server.
POST: Send data to the server to create a new resource.
PUT: Update an existing resource.
DELETE: Remove a resource.

HTTP Headers:
Headers provide essential information about the request and response, such as content type, authorization, and more.

Status Codes:
HTTP status codes are issued by the server to indicate the outcome of a request. Common ones include:

200 OK: Successful request.
301: Redirected
404 Not Found: Resource not found.
500 Internal Server Error: Server encountered an error.
201 Created: Resource created successfully.
"""

#Setting up Flask
pip install Flask

#Basic Flask App Setup
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a basic route
@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)


"""
Flask(__name__): Initializes a Flask app.
@app.route('/'): Defines a route, which is the URL at which this function will be accessible. The home() function is mapped to the root (/) URL.
app.run(debug=True): Runs the app in debug mode, which helps in development.
"""

#Run the app by executing:
#python app.py

#HTTP Methods and Status Codes
#Let's build routes that use different HTTP methods, return responses, and include appropriate status codes.

#GET Method:
#This method is used to retrieve data.
@app.route('/get_data', methods=['GET'])
def get_data():
    data = {"message": "This is a GET request"}
    return data, 200  # 200 OK status code

#POST Method:
from flask import request

@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.get_json()  # Get data from the request body (JSON)
    return {"message": "Data received", "data": data}, 201  # 201 Created status code

#PUT Method:
#Used for updating an existing resource.
@app.route('/update_data', methods=['PUT'])
def update_data():
    data = request.get_json()
    # Logic to update the data...
    return {"message": "Data updated successfully"}, 200  # 200 OK status code

#DELETE Method:
#Used to delete an existing resource.
@app.route('/delete_data', methods=['DELETE'])
def delete_data():
    return {"message": "Data deleted successfully"}, 200  # 200 OK status code


#HTTP Headers
#Headers provide important information about the request or response. In Flask, you can set headers in the response.
@app.route('/set_header')
def set_header():
    response = "This is a response with custom headers"
    return response, 200, {'X-Custom-Header': 'FlaskExample'}

#Sample RestAPI
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data
users = {
    1: {"name": "Alice", "age": 25},
    2: {"name": "Bob", "age": 30}
}

# GET method to retrieve a user
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    else:
        return {"message": "User not found"}, 404

# POST method to create a new user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()  # Get data from the request body
    user_id = len(users) + 1  # Simple ID generation
    users[user_id] = data
    return {"message": "User created", "user": data}, 201

# PUT method to update a user
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if user:
        data = request.get_json()
        users[user_id] = data
        return {"message": "User updated", "user": data}, 200
    else:
        return {"message": "User not found"}, 404

# DELETE method to delete a user
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return {"message": "User deleted"}, 200
    else:
        return {"message": "User not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)
