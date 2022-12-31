import pip._vendor.requests

response = pip._vendor.requests.get('http://127.0.0.1:8000/drinks')
print(response.json())