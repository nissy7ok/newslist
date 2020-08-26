from django.urls import path, include
from . import views
from .views.views import mypage, StockNews, delete_stock, exec_ajax
from .views.index import index

app_name='newslistapp'
urlpatterns = [
    path('', index, name='index'),
    path('mypage/', mypage, name='mypage'),
    path('stock/', StockNews.as_view(), name='stock'),
    path('delete_stock/<int:pk>/', delete_stock, name='delete_stock'),
    # Ajax処理
    path("exec/", exec_ajax, name='exec'),
]
