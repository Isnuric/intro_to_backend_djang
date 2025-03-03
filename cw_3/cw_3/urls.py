from django.contrib import admin
from django.urls import path, include
from post.views import home_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'),
    path('', include('post.urls')),
]
