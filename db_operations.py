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
            password= conn_params['Password'],
            host= conn_params['Host'],  
            port= conn_params['Port']
        )
    except Exception as e:
        print(f"Error in database connection: {e}")
    return connection

def processed_data(column_names, rows):
    processed_rows = []
    for row in rows:
        processed_row = {}
        for index, column  in enumerate(column_names):
            processed_row[column] = row[index]
            # in first loop item would be like 
            # {'name': 'BMW', 'owner': 'John', 'year': 2020}

            # in second loop item would be like
            # {'name': 'BMW', 'owner': 'John', 'year': 2020, 'color': 'red'}

        processed_rows.append(processed_row)

    return processed_rows

def selectTableRows(query):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    # processing data before sending to caller 
    column_names = [desc[0] for desc in cur.description]
    final_data = processed_data(column_names, rows)

    cur.close()
    conn.close()
    return final_data

def insertUpdateDeleteRow(query, *params):
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(query, params)  
    conn.commit()
    cur.close()
    conn.close()


#______________________________________________________________________________________________
# if __name__ == '__main__': 
#     # query = "SELECT name, owener, year FROM cars;"
#     print(selectTableRows(query))