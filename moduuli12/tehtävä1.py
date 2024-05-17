import requests

def fetch_joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    data = response.json()
    return data['value']

print(fetch_joke())