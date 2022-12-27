import requests

from bs4 import BeautifulSoup


url = "https://meteoinfo.ru/forecasts/turkey/izmiradnan"
response = requests.get(url)
bs = BeautifulSoup(response.text, features="html.parser") # создаем обьект bs

temp = bs.find('span', class_="fc_temp_short") # ищем класс, отвечающий за погоду.

print("В Кушадасы сегодня днем:", temp.text)
