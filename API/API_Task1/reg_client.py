
import requests

url = "http://127.0.0.1:8000/register"

# User information
data = {
    "username": "amit",
    "email": "amit@gmail.com",
    "password": "python123"
}

# Send POST request
response = requests.post(url, json=data)

# Display response
print("Status Code:", response.status_code)
print("Response:", response.json())
