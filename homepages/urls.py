"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from homepages import views

app_name = 'homepages'
urlpatterns = [
    url(r'^$',                         views.home_page,   name='home'),
    url(r'^datetime$',              views.date_time,  name='datetime'),
    # url(r'^firstLoughe',          views.firstLoughe,    name='firstLoughe'),
    # url(r'^newLounge',          views.newLounge,   name='newLounge'),
    # url(r'^myFirstJavaScript',  views.myFirstJavaScript,  name='myFirstJavaScript'),
    # url(r'^json',                    views.json,             name='json'),
    # # url(r'^webui',                  webui.draw_picture, name='show_picture'),
]
