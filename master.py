import requests
link = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=10&tsym=EUR"
odbior = requests.get(link)
odbior.status_code
odbior.text
odbior.json()
print (odbior.status_code)