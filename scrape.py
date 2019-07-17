from urllib import request
import requests
from bs4 import BeautifulSoup
import csv
import time

header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        }
url = 'https://tabelog.com/tokyo/rstLst/CC02/'
count = 1

targets = []

class target_shop:
    def __init__(self):
        pass
    id = int()
    shopname = ''
    url = ''
    rate = ''
    station = ''
    comment = ''
    smoke = ''

id_count = 1

while(True):
    time.sleep(1)
    ret = requests.get(url + str(count), headers = header)
    if ret.status_code == 400:
        print("fuck")
        break

    soup = BeautifulSoup(ret.content, 'html.parser')
    list = soup.find_all("div", class_='list-rst__wrap js-open-new-window')

    for li in list:
        target = target_shop()
        target.id = id_count
        id_count += 1

        shops = li.find_all("a", class_="list-rst__rst-name-target cpy-rst-name")
        comments = li.find_all('p', class_="list-rst__pr-title cpy-pr-title")
        stations  = li.find_all('span', class_='list-rst__area-genre cpy-area-genre')
        rates = li.find_all('span', class_="c-rating__val c-rating__val--strong list-rst__rating-val")

        for shop in shops:
            print("shopname : {}".format(shop.text))
            print("url      : {}".format(shop.get("href")))
            target.shopname = shop.text
            target.url = shop.get("href")

        for station in stations:
            print("station  : {}".format(station.text))
            target.station = station.text

        for comment in comments:
            print("comment  : {}".format(str(comment.text).strip()))
            target.comment = str(comment.text).strip()

        for rate in rates:
            print("rate     : {}".format(rate.text))
            target.rate = rate.text

        smoke = li.find_all("li", class_="list-rst__search-word-item")
        for item in smoke:
            if ("分煙" in item.text):
                print("item     : 分煙")
                target.smoke = '分煙'
            if ("完全禁煙" in item.text):
                print("item     : 完全禁煙")
                target.smoke = '完全禁煙'
            if ('喫煙可' in item.text):
                print("smoking  : 喫煙可")
                target.smoke = '喫煙可'
        print("-------------------------------------------{}".format(count))
        targets.append(target)
    count += 1

with open('coffeeList.csv','a') as f:
    writer = csv.writer(f)
    for target in targets:
        writer.writerow([
        target.id,
        target.shopname,
        target.url,
        target.rate,
        target.station,
        target.comment,
        target.smoke])
