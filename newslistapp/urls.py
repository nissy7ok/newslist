from django.urls import path, include
from . import views
from .views import index, mypage, StockNews, delete_stock

app_name='newslistapp'
urlpatterns = [
    path('', index, name='index'),
    path('mypage/', mypage, name='mypage'),
    path('stock/', StockNews.as_view(), name='stock'),
    path('delete_stock/<int:pk>/', delete_stock, name='delete_stock'),
]
