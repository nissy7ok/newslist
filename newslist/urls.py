from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('', include('newslistapp.urls', namespace='newslistapp')),
    path('admin/', admin.site.urls),
]
