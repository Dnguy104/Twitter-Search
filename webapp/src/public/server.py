from flask import Flask, request, jsonify
from flask_cors import CORS
import indexer
import searcher
import settings
import json

app = Flask(__name__)
CORS(app)

incomes = [
  { 'description': 'salary', 'amount': 5000 },
  { 'description': 'salary', 'amosunt': 6000 },
  { 'description': 'poopoo', 'amount': 7000 }
]

@app.route('/hello', methods = ['GET', 'POST'])
def hello():
  all_args = request.args.lists()
  # print(all_args[0][0])
  # print(all_args[0][1][0])
  q = all_args[0][1][0]
  return jsonify(searcher.search_files(q))
  # return jsonify(all_args)

@app.route('/world', methods = ['GET', 'POST'])
def world():
  return jsonify(indexer.index_files())
  # return jsonify(all_args)

if __name__ == '__main__':
    app.run(debug = True)
