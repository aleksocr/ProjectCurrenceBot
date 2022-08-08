
TOKEN = '5481293929:AAHhTw68wowVfCjKsT1krtz1f_ahfxDVfsk'

# import requests
# import bs4
# from bs4 import BeautifulSoup as bs
# b = bs
# url = 'https://belarusbank.by/ru/fizicheskim_licam/valuta/kursy-valyut'
# r = requests.get(url)
# soup = bs4.BeautifulSoup(r.text, "html.parser")
# print(soup.title)
# # курс продаж
# mags = soup.select('td')
# print(mags[4])
#
#
# import requests
# data = requests.get('https://belarusbank.by/api/kursExchange?/latest.json?app_id=YOUR_APP_ID').json()
# print(data[int()])


import requests
from bs4 import BeautifulSoup

url = 'https://m.myfin.by/currency/minsk'
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML) Version/13.0.3 Mobile/15E148 Safari/604.1'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

usd = soup.find('div', class_='bl_usd_ex').text
eur = soup.find('div', class_='bl_eur_ex').text

