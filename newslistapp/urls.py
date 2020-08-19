from django.urls import path
from . import views
from .views import index, mypage, StockNews

app_name='newslistapp'
urlpatterns = [
    path('', index, name='index'),
    path('mypage/', mypage, name='mypage'), # <int:id>/あとでたす
    path('stock/', StockNews.as_view(), name='stock')
]
