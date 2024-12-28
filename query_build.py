SELECT_ROWS = "SELECT * FROM #table_name"
SELECT_SPECIFIC_ROW = "SELECT * FROM #table_name WHERE id = #id;"



# Insert Queries
INSERT_LEARNING_ENTRY = "INSERT INTO learning_entries (date, learning) VALUES (%s, %s);"
INSERT_SUBJECT = "INSERT INTO subjects (name, optional, description) VALUES (%s, %s, %s)"


# Update Queries
UPDATE_LEARNING_ENTRY = "UPDATE learning_entries SET date = %s, learning = %s WHERE id = %s;"
UPDATE_SUBJECT = "UPDATE subjects SET name = %s, optional = %s, description = %s WHERE id = %s;"


# Delete Query
ALL_DELETE_LEARNING_ENTRIES = "DELETE FROM learning_entries;"
ALL_DELETE_SUBJECTS = "DELETE FROM subjects;"
DELETE_LEARNING_ENTRY = "DELETE FROM learning_entries WHERE id = %s;"
DELETE_SUBJECT = "DELETE FROM subjects WHERE id = %s;"


# ==============================================================================

def build_select_all_query(table_name):
    final_query = SELECT_ROWS.replace("#table_name", table_name)
    print(final_query)
    return final_query


def build_select_specific_query(table_name, id):
    final_query = SELECT_SPECIFIC_ROW.replace("#table_name", table_name)
    final_query = final_query.replace("#id", id)
    print(final_query)
    return final_query


#______________________________________________________________________________________________
if __name__ == '__main__': 
    build_select_all_query('inventory')