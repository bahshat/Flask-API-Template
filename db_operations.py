import json
import psycopg2
from datetime import datetime

with open('database_connection.json') as f:
    conn_params = json.load(f)
    
# ________________________________________________________________________________
def db_connection():
    try:
        connection = psycopg2.connect(
            dbname= conn_params['MaintenanceDB'],
            user= conn_params['Username'],
            password="AVNS_jj25SnhUAlU7PzpfngP",
            host= conn_params['Host'],  
            port= conn_params['Port']
        )
    except Exception as e:
        print(f"Error in database connection: {e}")
    return connection

def selectTableRows(query):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def insertUpdateDeleteRow(query, *params):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query, params)  
    conn.commit()
    cur.close()
    conn.close()