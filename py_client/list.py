import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
password = getpass()

auth_response = requests.post(endpoint, json={"username":"2882","password":password})
print(auth_response.json())


endpoint = "http://localhost:8000/api/products/"
get_response = requests.get(endpoint)
print(get_response.json())