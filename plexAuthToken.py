import requests
import json

username = input("Enter your plex email address: ")
password = input("Enter your plex password: ")
client = input("Enter Client Name: ")
version = input("Enter Version number: ")

url = 'https://plex.tv/users/sign_in.json'
headers = {
"X-Plex-Client-Identifier": client,
"X-Plex-Product": client,
"X-Plex-Version": version
}

res = requests.request("POST", url, headers=headers, auth=(username, password))
data = json.loads(res.content)
print(f"The Auth Token for {client} is: {data['user']['authToken']}")
