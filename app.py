from flask import Flask, jsonify, request
from db_operations import *
from db_queries import *
from query_build import *
app = Flask(__name__)


#________________________________ GET HTTP methods _______________________________________

@app.route('/table/<string:table_name>', methods = ["GET"])
def getAllData(table_name):
    query = build_select_all_query(table_name)
    result = selectTableRows(query)
    return (jsonify(result))


@app.route('/table/<string:table_name>/<int:id>', methods = ["GET"])
def getSpecificData(table_name, id):
    query = build_select_specific_query(table_name, id)
    result = selectTableRow(query, id)
    return (jsonify(result))


#______________________________________________________________________________________________
if __name__ == '__main__': 
    app.run(debug=True)