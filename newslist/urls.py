from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('index/', include('newslistapp.urls'), name='newslistapp'),
    path('admin/', admin.site.urls),
]
