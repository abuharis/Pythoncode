# import json
# from flask import Flask, jsonify, request, render_template
# app = Flask(__name__)

# employees = [
#  { 'id': 1, 'name': 'Ashley' },
#  { 'id': 2, 'name': 'Kate' },
#  { 'id': 3, 'name': 'Joe' },
#  {'id': 4, 'name': 'Maria'},
#  {'id': 5, 'name': 'neew uswer'}
# ]


"""Json Dumps is used to dump a dict into string, whereas dump is used to dump a dict into a file"""
# nextEmployeeId = 5


# @app.route('/')
# def hello_world():
#   return render_template('login.html')

# # @app.route('/employees', methods=['GET'])
# # def get_employees():
# #  return jsonify(employees)

# @app.route('/employees/<int:id>', methods=['GET'])
# def get_employee_by_id(id: int):
#  employee = get_employee(id)
#  if employee is None:
#    return jsonify({ 'error': 'Employee does not exist'}), 404
#  return jsonify(employee)


# @app.route('/employees', methods=['POST'])
# def create_employee():
#   global nextEmployeeId
#   employee = json.load(request.data)

  
#   employee['id'] = nextEmployeeId
#   nextEmployeeId += 1
#   employees.append(employee)


# @app.route('/render', methods= ['POST'])
# def render_file():
#   return "hai"


# def get_employee(id):
#  return next((e for e in employees if e['id'] == id), None)





# if __name__ == '__main__':
#    app.run(port=5000)


from flask import Flask, render_template, request, jsonify, json


app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api-endpoint', methods=['POST', 'GET'])
def handle_api_request():
    try:
        # Assuming the payload is JSON
        data = request.json
        # Process the data as needed
        # ...

        # Return a sample response
        response_data = {'status': 'success', 'message': 'Request processed successfully'}
        return jsonify(response_data)
    except Exception as e:
        # Handle exceptions
        response_data = {'status': 'error', 'message': str(e)}
        return jsonify(response_data), 500
    

@app.route('/signin', methods=['POST'])
def handle_new_request():
    username = request.form['username']
    password = request.form['password']

    if username and password:
        return json.dumps({'validation':  validateUser(username, password)})
    

def validateUser(username, password):
    if username == "abuharis":
      return True
    else:
        return True


app.run(debug=True)
    

# new = {
#    "responseStatus": "fail",
#    "responseHeader": {
#      "now": 1465840430014,
#      "status": "fail",
#      "requestId": True
#    },
#    "responseData": {
#      "validationErrors": [
#        {
#          "category": "Vault Existence",
#          "rule": "Only service or management vaults may exist",
#          "objects": []
#        },
#        {
#          "category": "API",
#          "rule": "access pool(s) must change its API type to 'Cloud Storage Object'",
#          "objects": [
#            {
#              "type": "accessPool",
#              "id": 8,
#              "name": "Access Pool 3"
#            }
#          ]
#        },
#        {
#          "category": "Mirror",
#          "rule": "Container Mode not supported on dsNets with mirrors",
#          "objects": []
#        }
#      ],
#      "migrationErrors": []
#    }
#  } 

# print(json.dumps(new['responseData']['validationErrors'][1], indent = 4))