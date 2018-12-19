from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from django.conf import settings

import  os
import re

from book.models import  Publisher, Author, Book, file_dir_path

# Create your views here.


class PublisherList(ListView):

    model = Publisher
    context_object_name = '出版商'


class PublisherDetail(DetailView):

    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context


class PublisherBookList(ListView):

    template_name = 'book/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = self.publisher
        return context


class BookList(ListView):
    queryset = Book.objects.order_by('publication_date')
    context_object_name = 'book_list'


def index(request):
    return render(request, 'homepages/index.html')


def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    authors = Author.objects.filter(book__id=id)
    return render(request, 'book/book_detail.html', {'book': book, 'authors':authors})


def book_read(request, id):
    line_per_page = 1000              #每页显示的行数

    book = get_object_or_404(Book, pk=id)
    filepath = file_dir_path(book)
    file = os.path.join(settings.MEDIA_ROOT, filepath.replace('/', '\\'))

    with open(str(file), encoding='utf-16') as f:
        contents = []
        count = 0

        regEx = r"第[\u4E00-\u9FA5]+章";
        pattern = re.compile(regEx)

        for line in f:
            match = pattern.match(line)
            if match:
                contents.append(match.group())

            contents.append(line.strip())
            count += 1
            if count > line_per_page: break
    return render(request, 'book/book_read.html', {'book': book, 'contents': contents})
