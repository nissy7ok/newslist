from django.urls import path
from . import views
from .views import signup

app_name = 'accounts'
urlpatterns = [
    path('signup/', signup, name='signup'),
]