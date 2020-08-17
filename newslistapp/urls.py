from django.urls import path
from . import views
from .views import index, mypage

urlpatterns = [
    path('', index, name='index'),
    path('mypage/', mypage, name='mypage'), # <int:id>/あとでたす
]
