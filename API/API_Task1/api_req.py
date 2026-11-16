#pip install requests

import requests

# API URL
url = "http://127.0.0.1:8000/mul"

# Data to send
data = {
    "a": 6,
    "b": 4
}

# Send POST request
response = requests.post(url, json=data)

# Display response
print("Status Code:", response.status_code)
print("Response:", response.json())
