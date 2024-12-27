
import pyodbc
from collect_token import fetch_token_from_database


query = "SELECT CustomerToken FROM dbo.Customers WHERE CustomerId = 79"
raw_token = fetch_token_from_database(query)


small_text = raw_token[0][0].lower().strip()
large_text = raw_token[0][0].upper().strip()

token = small_text

print(small_text)


get_ID = "1593DA6E-2A1A-4D45-BF6E-5246BA9AFE70"

small_ID = get_ID.lower().strip()

print(small_ID)