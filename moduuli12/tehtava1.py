import requests

try:
    joke = requests.get('https://api.chucknorris.io/jokes/random')
    if joke.status_code==200:
        print(joke.json()['value'])
except requests.exceptions.RequestException as e:
    print('Chuck Norris could not find the joke.')