
TOKEN = '5481293929:AAHhTw68wowVfCjKsT1krtz1f_ahfxDVfsk'

import requests
from bs4 import BeautifulSoup

url = 'https://m.myfin.by/currency/minsk'
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML) Version/13.0.3 Mobile/15E148 Safari/604.1'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, 'html.parser')

usd = soup.find('div', class_='bl_usd_ex').text
eur = soup.find('div', class_='bl_eur_ex').text

