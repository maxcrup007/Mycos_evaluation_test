
from urllib.parse import urlparse

with open("Collect_Text/link.text") as file:
            link = file.read()

parsed_url = urlparse(link)

# Extract components
hostname = parsed_url.hostname
path = parsed_url.path
query = parsed_url.query

path_segments = path.strip("/").split("/")

first_segment = path_segments[0]  
token_segment = path_segments[-1] 

print(f"Hostname: {hostname}")  
print(f"Path: {path}")
print(f"First Segment: {first_segment}")
print(f"Last Segment: {token_segment}")
print(f"Query: {query}")   

url = "https://" + hostname + path + "?month=11&year=2024"


print(url)








