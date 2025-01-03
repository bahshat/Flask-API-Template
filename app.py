from flask import Flask, jsonify, request
from db_operations import *
from query_build import build_query

app = Flask(__name__)

#________________________________ HTTP methods _______________________________________

@app.route('/table/<string:table_name>', methods = ["GET"])
def getData(table_name):
    id = request.args.get('id')
    query = build_query("select", table_name, {}, id)
    result = selectTableRows(query)
    return (jsonify(result))


@app.route('/table/<string:table_name>', methods = ["DELETE"])
def deleteData(table_name):
    id = request.args.get('id')
    query = build_query("delete", table_name, {}, id)
    result = insertUpdateDeleteRow(query, id)
    return (jsonify(result))


@app.route('/table/<string:table_name>', methods = ["POST"])
def insertData(table_name):
    body = request.get_json()
    
    query = build_query("insert", table_name, body, None)

    result = insertUpdateDeleteRow(query)

    return (jsonify(result))


@app.route('/table/<string:table_name>', methods = ["PUT"])
def updateData(table_name):
    id = request.args.get('id')
    body = request.get_json()
    query = build_query("update", table_name, body, id)
    result = insertUpdateDeleteRow(query)
    return (jsonify(result))

#______________________________________________________________________________________________
if __name__ == '__main__': 
    app.run(debug=True)