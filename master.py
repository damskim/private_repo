import requests
import json
link = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=10&tsym=EUR"
odbior = requests.get(link)
odbior.status_code
print (odbior.status_code)
parameters = []
krypto = input ("Podaj skrot krypto do wyfiltrowania:")
krypto = krypto.upper()
parameters.append(krypto)
odbior.text
odbior.json()
print (parameters)
#print (odbior.json())
