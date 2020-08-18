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
    articles = Article.objects.all()
    target = "新R25"
    url = "https://r25.jp/latest"
    url_pattern = "https?://[^/]+/"
    m = re.match(url_pattern, url)
    favicon = m.group() + "favicon.ico"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.find_all(href=re.compile("/article/"))

    news_list = []
    for elem in elems:
        title = elem.h3.string
        date = elem.time.string
        date = dt.strptime(date, '%Y.%m.%d').date()
        path = elem.attrs["href"]
        url = "https://r25.jp" + path
        news_list.append([title, date, url])

    return render(request, 'index.html', {'target': target, 'favicon': favicon, 'news_list': news_list, 'articles': articles})

def mypage(request):
    articles = Article.objects.all()
    return render(request, 'mypage.html', {'articles': articles})
    # user_idでページを分ける
