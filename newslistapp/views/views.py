from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from ..models import Article

from django.http.response import JsonResponse


@login_required
def mypage(request):
    """マイページへ一覧表示するためのリストを作成
    """
    articles = Article.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'mypage.html', {'articles': articles})

class StockNews(CreateView, LoginRequiredMixin):
    """ニュースをマイページへ保存するためのメソッド
    """
    template_name = 'index.html'
    model = Article
    fields = ('user', 'title', 'name', 'url', 'icon')
    success_url = reverse_lazy('newslistapp:index')

@login_required
@require_POST
def delete_stock(request, pk):
    """マイページに保存した記事を削除するためのメソッド
    """
    stock = get_object_or_404(Article, pk=pk)
    stock.delete()
    return redirect('newslistapp:mypage')
