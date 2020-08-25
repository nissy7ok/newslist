from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.contrib import messages
# from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Article
# import logging
from django.http.response import JsonResponse

# スクレイピング関係
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
from concurrent.futures import ThreadPoolExecutor
from functools import partial

# logger = logging.getLogger('development')

def index(request):
    articles = Article.objects.all()
    
    icons = {
        'programing': 'p',
        'marketing': 'm',
        'entertainment': 'e',
        'news': 'n'}

    urls = [
        'https://r25.jp/latest',
        'https://ai-trend.jp/',
        'https://markezine.jp/',
        'https://prtimes.jp/'
    ]

    results = []
    for url in urls:
        r = requests.get(url, timeout=(3.0, 7.5))
        results.append(r)

    # 新R25
    soup = BeautifulSoup(results[0].text, "html.parser")
    elems = soup.find_all(href=re.compile("/article/"))

    news_list = []
    for elem in elems[:5]:
        target = '新R25'
        icon = icons['news']
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
    elems3 = soup3.find_all(class_='new')

    for elem in elems3[:5]:
        target = 'MarkeZine'
        icon = icons['marketing']
        title = elem.a.text.strip()
        date = elem.a.text.strip()
        date = dt.strptime(date[-7:], '（%m/%d）')
        year_n = dt.now().year
        date = str(year_n) + date.strftime('%m%d')
        date = dt.strptime(date, '%Y%m%d').date()
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
        date = dt.now().date()
        path = elem.a.attrs["href"]
        url = "https://markezine.jp/" + path
        news_list.append([target, icon, title, date, url])

    news_list = sorted(news_list, key=lambda x: x[3], reverse=True)
    return render(request, 'index.html', {'news_list': news_list, 'articles': articles})

@login_required
def mypage(request):
    articles = Article.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'mypage.html', {'articles': articles})

class StockNews(CreateView, LoginRequiredMixin):
    template_name = 'index.html'
    model = Article
    fields = ('user', 'title', 'name', 'url', 'icon')
    success_url = reverse_lazy('newslistapp:index')
    # def form_valid(self, form):
    #     messages.success(self.request, "記事を保存しました")
    #     return super().form_valid(form)
    # def form_invalid(self, form):
    #     messages.warning(self.request, "記事は既に保存されています")
    #     return redirect('newslistapp:index')

@login_required
@require_POST
def delete_stock(request, pk):
    # title = Article.objects.values_list('title', flat=True).get(pk=pk)
    # for stock in Article.objects.filter(title=title).filter(user=request.user):
    #     stock.delete()
    stock = get_object_or_404(Article, pk=pk)
    stock.delete()
    return redirect('newslistapp:mypage')

# Ajax処理
def exec_ajax(request):
    if request.method == 'POST':  # POSTの処理
        data1 = request.POST.get("user")  # POSTで渡された値
        data2 = request.POST.get("title")  # POSTで渡された値
        data3 = request.POST.get("name")  # POSTで渡された値
        data4 = request.POST.get("url")  # POSTで渡された値
        data5 = request.POST.get("icon")  # POSTで渡された値
        # article = Article(user = data1, title = data2, url = data3, name = data4, icon = data5, created_at = dt.now)
        # article.save()
        # logger.debug(data1 + data2 + data3 + data4 + data5)
        return HttpResponse(data2)