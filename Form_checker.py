import pyodbc

 
def fetch_form_check_database(query):
    server = 'dev-mycos.database.windows.net'  
    database = 'MycosCenterDB_Dev' 
    username = 'mycosSA' 
    password = 'mycos234!@#' 
    connection = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()  
    connection.close()
    return results

query = "select IsComplete  from EvaluateForm where CustomerBy = 78"
data = fetch_form_check_database(query)

print(data)


   



