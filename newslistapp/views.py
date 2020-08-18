from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Article

# スクレイピング関係
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

def index(request):
    articles = Article.objects.all()    # 保存用DB、まだ使わない
    
    targets = ['新R25', 'AVILEN AI Trend']
    urls = {
        targets[0]: 'https://r25.jp/latest',
        targets[1]: 'https://ai-trend.jp/'
    }

    # 新R25
    url = 'https://r25.jp/latest'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.find_all(href=re.compile("/article/"))

    news_list = []
    for elem in elems:
        target = '新R25'
        icon ='新'
        title = elem.h3.text
        date = elem.time.text.strip()
        date = dt.strptime(date, '%Y.%m.%d').date()
        path = elem.attrs["href"]
        url = "https://r25.jp" + path
        news_list.append([target, icon, title, date, url])

    # AVILEN AI Trend
    url2 = 'https://ai-trend.jp/'
    res2 = requests.get(url2)
    soup2 = BeautifulSoup(res2.text, "html.parser")
    elems2 = soup2.find_all(class_='article__content')

    for elem in elems2:
        target = 'AVILEN AI Trend'
        icon = 'A'
        title = elem.h3.text.strip()
        date = elem.p.string
        date = dt.strptime(date, '%Y.%m.%d %a').date()
        url = elem.a.attrs["href"]
        news_list.append([target, icon, title, date, url])

    news_list = sorted(news_list, key=lambda x: x[3], reverse=True)
    return render(request, 'index.html', {'news_list': news_list, 'articles': articles})

def mypage(request):
    articles = Article.objects.all()
    return render(request, 'mypage.html', {'articles': articles})
    # user_idでページを分ける
