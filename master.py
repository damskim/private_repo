import requests
import json

url = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=10&tsym=EUR"
response = requests.get(url)
big_data = requests.get(url).json()
response.text
open("response.json", "wb").write(response.content)

#SPRAWDZANIE STATUSU API
#print (response['Type'])

#PARAMETRY WYSZUKIWANIA
#parameters = []
#krypto = input ("Podaj skrot krypto do wyfiltrowania:")
#krypto = krypto.upper()
#parameters.append(krypto)
#print (parameters)


for item in big_data['Data']:
    item_name = item['CoinInfo']['Name']
    item_fullname = item['CoinInfo']['FullName']
    item_entrydate = item['CoinInfo']['AssetLaunchDate']
    item_price = item['DISPLAY']['EUR']['PRICE']
    item_highday = item['DISPLAY']['EUR']['HIGHDAY']
    item_lowday = item['DISPLAY']['EUR']['LOWDAY']
    print(item_name)
    print(item_fullname)
    print(item_price)
    print(item_highday)
    print(item_lowday)
    print(item_entrydate)
    print("Nowe krypto")
#print (big_data['Data'][0])