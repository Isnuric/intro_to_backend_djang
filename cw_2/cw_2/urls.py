from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Басты бетті автоматты түрде /posts/ бетіне бағыттау
def home_redirect(request):
    return redirect('post_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home'),  # Басты бетті post_list-қа бағыттау
    path('', include('post.urls')),
]
