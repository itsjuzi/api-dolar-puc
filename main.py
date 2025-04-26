import requests
import time

moeda_origem = 'USD'
moeda_destino = 'BRL'

host = f'https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}'
req = requests.get(host)

print(req.json()[f"{moeda_origem}{moeda_destino}"]["bid"])

time.sleep(10)