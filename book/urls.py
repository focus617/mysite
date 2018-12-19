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
from django.urls import  path

from book import views

app_name = 'book'
urlpatterns = [
    url(r'^$',                              views.BookList.as_view()),
    path('publishers',                    views.PublisherList.as_view(),  name='publisher_list'),
    # path('books',                         views.BookList.as_view(),       name='books_list'),
    path('books',                          views.book_list,                    name='books_list'),
    url(r'^books/(\d+)$',             views.book_detail,                 name='book_detail'),
    url(r'^books/reader/(\d+)$',   views.book_read,                  name='book_read'),
]
