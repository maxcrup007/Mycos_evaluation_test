import pyodbc

def fetch_token_from_database(query):
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

query = "select CustomerToken from dbo.Customers where CustomerId = 79"
data = fetch_token_from_database(query)

with open("Collect_Text/token.text", "w") as file:
            file.write(str(data))
            print(str(data))
    
      






