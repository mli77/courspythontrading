import requests

# Define your Firebase Realtime Database URL
DATABASE_URL = "URL_FIREBASE"

# Send data to the database
data_to_send = [
    {"data": "ma donnee", "high": 34, "low": 32, "close": 33},
    {"data2": "ma donnee2"},
    {"data3": "ma donnee3"}
]
response = requests.post(DATABASE_URL + "cours.json", json=data_to_send)
print("Data sent:", response.json())

# Retrieve data from the database
response = requests.get(DATABASE_URL + "cours.json")
data_received = response.json()
print("Data received:", data_received)