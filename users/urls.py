from django.urls import path
from . import views
from .views import signup

app_name = 'users'
urlpatterns = [
    path('signup/', signup, name='signup'),
]