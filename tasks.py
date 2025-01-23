from flask import Flask, jsonify, request, json

app = Flask(__name__)

database = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25},
    "user3": {"name": "Charlie", "age": 35}
}

@app.route('/')
def say_hello():
    return jsonify({"message": "Welcome to my applicaiton"})

@app.route('/users', methods=['GET'])
def get_all_users():
    users = []
    for user_id, user_data in database.items():
        user_name = user_data.get('name')  # Get the name 
        if user_name is not None:  # Check for None 
            # ... further processing with user_name ...
            users.append(user_data) 
    return jsonify(users)

@app.route('/get_data/<key>')
def get_data(key):
    """
    Retrieves data associated with the given key from the sample database.

    Args:
        key (str): The key to look up in the database.

    Returns:
        jsonify: A JSON response containing the data associated with the key, 
                 or an error message if the key is not found.
    """
    if key in database:
        return jsonify(database[key])
    else:
        return jsonify({"error": f"Key '{key}' not found in database."}), 404
    
@app.route('/update_user/<key>', methods=['PUT'])
def update_user(key):
    """
    Updates an existing user in the database.

    Args:
        key (str): The key of the user to update.

    Returns:
        jsonify: A JSON response indicating success or failure.
    """
    if key not in database:
        return jsonify({"error": f"User '{key}' not found."}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided in request body."}), 400

    # Update user data
    database[key].update(data)

    return jsonify({"message": f"User '{key}' updated successfully."})

@app.route('/new_user', methods=['POST'])
def create_user():
    """
    Creates a new user in the database.

    Returns:
        jsonify: A JSON response indicating success or failure.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided in request body."}), 400

    # Check if a user with the same key already exists
    if data.get('key') in database:
        return jsonify({"error": f"User with key '{data.get('key')}' already exists."}), 400

    # Add the new user to the database
    database[data.get('key')] = data

    return jsonify({"message": "User created successfully."})
# Flask class has a route method. The route method takes at least one argument, which is the endpoint also optionally method HTTP

app.run(debug=True)