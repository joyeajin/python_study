import requests

url = 'http://127.0.0.1:8000/hello'

params = {
    'name': 'yeajin~ ',
    'msg': 'hihi'
}

req = requests.get('http://127.0.0.1:8000/random_number')
req2 = requests.get('http://127.0.0.1:8000/hello?name=yeajin')
req3 = requests.get('http://127.0.0.1:8000/hello')
req4 = requests.get(url=url, params=params)

print(req4.status_code)
print(req4.text)