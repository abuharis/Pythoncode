from flask import Flask, jsonify, abort
from db import fetch_blogs, fetch_blog, NotFoundError, NotAuthorized

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World"

@app.route('/blogs')
def all_blogs():
  return jsonify(fetch_blogs())

@app.route('/blogs/<id>')
def get_blog(id):
  try:
    return jsonify(fetch_blog(id))
  except TypeError:
    abort(405, description="The resource you are looking for is not found in the db")

app.run()