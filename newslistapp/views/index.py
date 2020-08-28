from django.shortcuts import render
# スクレイピング関係
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from ..models import Article

def index(request):
    title_list = Article.objects.filter(user=request.user).values_list('title', flat=True)
    title_list = list(title_list)
    # アイコンを分類
    icons = {
        'programing': 'p',
        'marketing': 'm',
        'entertainment': 'e',
        'news': 'n',
        'improvement': 'i'
        }

    # ターゲットURL
    urls = [
        'https://r25.jp/latest',
        'https://ai-trend.jp/',
        'https://markezine.jp/news_pickup/',
        'https://prtimes.jp/',
        'https://ainow.ai/category/ainoweditor/'
    ]

    # マルチスレッド処理
    with ThreadPoolExecutor(4) as executor:
        results = list(executor.map(requests.get, urls))


    # 新R25
    soup = BeautifulSoup(results[0].text, "html.parser")
    elems = soup.find_all(href=re.compile("/article/"))

    news_list = []
    for elem in elems[:5]:
        target = '新R25'
        icon = icons['improvement']
        title = elem.h3.text
        date = elem.time.text.strip()
        date = dt.strptime(date, '%Y.%m.%d').date()
        path = elem.attrs["href"]
        url = "https://r25.jp" + path
        news_list.append([target, icon, title, date, url])


    # AVILEN AI Trend
    soup2 = BeautifulSoup(results[1].text, "html.parser")
    elems2 = soup2.find_all(class_='article__content')

    for elem in elems2[:5]:
        target = 'AVILEN AI Trend'
        icon = icons['programing']
        title = elem.h3.text.strip()
        date = elem.p.string
        date = dt.strptime(date, '%Y.%m.%d %a').date()
        url = elem.a.attrs["href"]
        news_list.append([target, icon, title, date, url])


    # MarkeZine
    soup3 = BeautifulSoup(results[2].text, "html.parser")
    elems3 = soup3.find_all(class_='boxWrap')

    for elem in elems3[:5]:
        target = 'MarkeZine'
        icon = icons['marketing']
        title = elem.a.text.strip()
        date = elem.find('span', class_='day').text
        date = dt.strptime(date, '%Y/%m/%d').date()
        path = elem.a.attrs["href"]
        url = "https://markezine.jp/" + path
        news_list.append([target, icon, title, date, url])


    # PR TIMES
    soup4 = BeautifulSoup(results[3].text, "html.parser")
    elems4 = soup4.find_all(class_='list-article')

    for elem in elems4[:5]:
        target = 'PR TIMES'
        icon = icons['marketing']
        title = elem.h3.text.strip()
        date = elem.time.attrs["datetime"]
        date = dt.strptime(date[:19], '%Y-%m-%dT%H:%M:%S').date()
        path = elem.a.attrs["href"]
        url = "https://prtimes.jp/" + path
        news_list.append([target, icon, title, date, url])


    # AINOW
    soup5 = BeautifulSoup(results[4].text, "html.parser")
    elems5 = soup5.find_all(class_='article')

    for elem in elems5[:5]:
        target = 'AINOW'
        icon = icons['programing']
        title = elem.h2.text.strip()
        date = elem.find('span', attrs={'class': 'article_date'}).text
        date = dt.strptime(date, '%Y.%m.%d').date()
        url = elem.find('a', class_='article_link').attrs["href"]
        news_list.append([target, icon, title, date, url])

    news_list = sorted(news_list, key=lambda x: x[3], reverse=True)
    return render(request, 'index.html', {'news_list': news_list, 'title_list': title_list})
