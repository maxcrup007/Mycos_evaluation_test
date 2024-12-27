import pyodbc

server = 'dev-mycos.database.windows.net'  
database = 'MycosCenterDB_Dev' 
username = 'mycosSA' 
password = 'mycos234!@#'  

# Connect to SQL Server
def connect_to_database():
    connection = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    return connection

# Fetch data from a table
def fetch_data_from_database(query):
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()  
    connection.close()
    return results


query = "Update EvaluateForm Set Comments = Null where CustomerBy = 78"
data = fetch_data_from_database(query)


for row in data:
    print(row)


