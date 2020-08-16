from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

def index(request):
    # return HttpResponse("Indexです！")
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

