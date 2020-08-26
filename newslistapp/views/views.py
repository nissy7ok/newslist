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
from ..models import Article
# import logging
from django.http.response import JsonResponse


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