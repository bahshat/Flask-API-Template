SELECT_ROWS = "SELECT * FROM #table_name"
DELETE_ROWS = "DELETE FROM #table_name"
INSERT_ROW = "INSERT INTO #table_name (#column_names) VALUES (#values);"
UPDATE_ROW = "UPDATE #table_name SET #set"
WHERE_CLOUSE = " WHERE id IN (#ids);"

# ==============================================================================

def build_insert_query(table_name, column_names, values):
    final_query = INSERT_ROW.replace("#table_name", table_name)

    final_column_names = ",".join(column_names) 
    final_values = ",".join([f"'{value}'" for value in values])

    final_query = final_query.replace("#column_names", final_column_names)
    final_query = final_query.replace("#values", final_values)

    return final_query

def build_select_query(table_name, ids):
    final_query = SELECT_ROWS.replace("#table_name", table_name)

    if ids: 
        where_clouse = WHERE_CLOUSE.replace("#ids", ids)
        final_query = final_query + where_clouse
    
    return final_query

def build_delete_query(table_name, ids):
    final_query = DELETE_ROWS.replace("#table_name", table_name)

    if ids:
        where_clouse = WHERE_CLOUSE.replace("#ids", ids)
        final_query = final_query + where_clouse
    
    return final_query

def build_update_query(table_name, data, ids):
    final_query = UPDATE_ROW.replace("#table_name", table_name)
    where_clouse = WHERE_CLOUSE.replace("#ids", ids)
    final_query = final_query + where_clouse
    
    final_set = ""

    for key, value in data.items():
        single_set = (f"{key} = '{value}',")
        final_set = final_set + single_set

    final_set = final_set[:-1]
    final_query = final_query.replace("#set", final_set)
    return final_query

# ==============================================================================
# Public functions
def build_query(query_type, table_name, data, ids):
    
    if query_type == "select":
        return build_select_query(table_name, ids)
    
    if query_type == "delete":
        return build_delete_query(table_name, ids)

    if query_type == "insert":
        return build_insert_query(table_name, data.keys(), data.values())

    if query_type == "update":
        return build_update_query(table_name, data, ids)
    
def build_select_some_query():
    
    query = "SELECT * FROM customer WHERE id IN (1, 2, 3);"

    return query
