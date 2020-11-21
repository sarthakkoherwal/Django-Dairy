"""DjangoDiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views


app_name = 'posts'
urlpatterns = [
    url(r'^postslist/$', views.post_list, name="list"),
    url(r'^create/$', views.post_create, name="create"),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='detail'),
    url(r'^delete/(?P<pk>\d+)/$', views.post_delete, name='post_delete'),
    url(r'^edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),

]
