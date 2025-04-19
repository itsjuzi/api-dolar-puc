import requests

host = f'https://economia.awesomeapi.com.br/last/USD-BRL'
req = requests.get(host)

print(req.json())