SELECT_ROWS = "SELECT * FROM #table_name"
DELETE_ROWS = "DELETE FROM #table_name"
INSERT_ROW = "INSERT INTO #table_name (#column_names) VALUES (#values);"
UPDATE_ROW = "UPDATE #table_name SET #set"
WHERE_CLOUSE = " WHERE id = #id;"

# ==============================================================================

def build_insert_query(table_name, column_names, values):
    final_query = INSERT_ROW.replace("#table_name", table_name)

    final_column_names = ",".join(column_names) 
    final_values = ",".join([f"'{value}'" for value in values])

    final_query = final_query.replace("#column_names", final_column_names)
    final_query = final_query.replace("#values", final_values)

    return final_query

def build_select_query(table_name, id):
    final_query = SELECT_ROWS.replace("#table_name", table_name)

    if id:
        where_clouse = WHERE_CLOUSE.replace("#id", id)
        final_query = final_query + where_clouse
    
    return final_query

def build_delete_query(table_name, id):
    final_query = DELETE_ROWS.replace("#table_name", table_name)

    if id:
        where_clouse = WHERE_CLOUSE.replace("#id", id)
        final_query = final_query + where_clouse
    
    return final_query

def build_update_query(table_name, data, id):
    final_query = UPDATE_ROW.replace("#table_name", table_name)
    where_clouse = WHERE_CLOUSE.replace("#id", id)
    final_query = final_query + where_clouse
    
    final_set = ""

    for key, value in data.items():
        single_set = (f"{key} = '{value}',")
        final_set = final_set + single_set

    final_set = final_set[:-1]
    final_query = final_query.replace("#set", final_set)
    return final_query