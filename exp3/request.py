import requests
response = requests.get("http://localhost:5001/users/1")
print(response.json())
