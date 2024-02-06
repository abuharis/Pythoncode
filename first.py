from  flask import Flask, jsonify, request, json

app = Flask(__name__)


# from app import index

employees = [ {
    'id': 1, 'name': 'Hai'
  } ]

# @app.route('/show', methods=['GET'])
# def get_employee():
#   return jsonify(employees)
@app.route('/debug', methods=['GET'])
def debug():
  print("it")


@app.route('/hai', methods=['GET'])
def get_employee_new():
  return jsonify(employees)

@app.route('/update', methods=['POST'])
def update_employee():
  data = request.json
  employees.append(data)
  response_data = json.dumps({'status': 'posted successfully'})

  return jsonify(response_data)


# def employee_is_valid(employees):
#   for key in employees.keys():
#     if key != "name":
#       print(False)


app.run(port=5000, debug=True)
