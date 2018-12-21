#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.test import TestCase
from book.models import Classfication, Author, Publisher, Book
from django.core.exceptions import ValidationError

# Create your tests here.


class BookModelTest(TestCase):

#     def test_saving_and_retrieving_books(self):
#         author = Author.objects.create(
#             first_name='Zhiyong', last_name='Xu', email='13980668829@163.com')
#         publisher = Publisher.objects.create(
#             name='Pub', country='China', website='http://www.pub.com')
#         classfication = Classfication.objects.create()
#
#         first_book = Book(classfication=classfication,
#                           publisher=publisher)
#         first_book.title = 'The first (ever) book'
#         first_book.save()
#         first_book.authors = (author,)
#         first_book.save()
#
#         second_book = Book(classfication=classfication,
#                            publisher=publisher)
#         second_book.title = 'The second book'
#         second_book.save()
#         second_book.authors = (author,)
#         second_book.save()
#
#         saved_book = Book.objects.first()
#         self.assertEqual(saved_book, first_book)
#
#         saved_books = Book.objects.all()
#         self.assertEqual(saved_books.count(), 2)
#
#         first_saved_book = saved_books[0]
#         second_saved_book = saved_books[1]
#         self.assertEqual(first_saved_book.title, 'The first (ever) book')
# #        self.assertContains(first_saved_book.authors, author)
#         self.assertEqual(first_saved_book.classfication, classfication)
#         self.assertEqual(first_saved_book.publisher, publisher)
#         self.assertEqual(second_saved_book.title, 'The second book')
#         self.assertEqual(second_saved_book.classfication, classfication)
#         self.assertEqual(second_saved_book.publisher, publisher)

    def test_cannot_save_empty_title_books(self):
        publisher = Publisher.objects.create(
            name='Pub', country='China', website='http://www.pub.com')
        classfication = Classfication.objects.create()

        book = Book(classfication=classfication,
                    publisher=publisher)
        book.title = ''
        with self.assertRaises(ValidationError):
            book.save()
            book.full_clean()
