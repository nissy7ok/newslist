from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def mypage(request):
    articles = Article.objects.all()
    return render(request, 'mypage.html', {'articles': articles})
    # user_idでページを分ける


