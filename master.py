import requests
import pandas as pd
import json

url = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=20&tsym=EUR"
response = requests.get(url)
big_data = requests.get(url).json()
response.text
open("response.json", "wb").write(response.content)
print("Witamy w CryptoCheckerze!")
#SPRAWDZANIE STATUSU API
print("--------------------")
print(f"Sprawdzenie odpowiedzi serwera danych: {response.status_code}")
print("--------------------")

#PARAMETRY WYSZUKIWANIA
#parameters = []
#krypto = input ("Podaj skrot krypto do wyfiltrowania:")
#krypto = krypto.upper()
#parameters.append(krypto)
#print (parameters)

#TWORZĘ SZABLON DANYCH

df = pd.DataFrame(columns=['item_fullname','item_name','item_price','item_lowday','item_highday','item_entrydate'])

#PĘTLA WYCIĄGAJĄCA DANE O KRYPTOWALUTACH Z OBIEKTÓW W API

for item in big_data['Data']:
    item_fullname = item['CoinInfo']['FullName']
    item_fullname = str(item_fullname)
    item_name = item['CoinInfo']['Name']
    item_name = str(item_name)
    item_price = item['DISPLAY']['EUR']['PRICE']
    item_price = item_price.replace(",", "")
    item_price = item_price.replace("€ ","")
    item_price = float(item_price)
    item_lowday = item['DISPLAY']['EUR']['LOWDAY']
    item_lowday = item_lowday.replace(",","")
    item_lowday = item_lowday.replace("€ ","")
    item_lowday = float(item_lowday)
    item_highday = item['DISPLAY']['EUR']['HIGHDAY']
    item_highday = item_highday.replace(",","")
    item_highday = item_highday.replace("€ ","")
    item_highday = float(item_highday)
    item_entrydate = item['CoinInfo']['AssetLaunchDate']
    item_entrydate = str(item_entrydate)
    df1 = pd.DataFrame({'item_fullname':item_fullname, 'item_name':item_name, 'item_price':item_price, 'item_lowday':item_lowday, 'item_highday':item_highday, 'item_entrydate':item_entrydate},ignore_index=True)
    df = pd.concat([df,df1])
    print(f"Nazwa kryptowaluty: {item_fullname}")
    print(f"Oznaczenie kryptowaluty: {item_name}")
    print(f"Aktualna cena: {item_price}")
    print(f"Najnizsza cena dzisiaj: {item_lowday}")
    print(f"Najwyzsza cena dzisiaj: {item_highday}")
    print(f"Data wejscia na rynek kryptowalut: {item_entrydate}")
    print("--------------------")
    print("Następna kryptowaluta")
    print("--------------------")
df