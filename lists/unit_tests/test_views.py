#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from unittest import skip

# Create your tests here.
from lists.views import lists_homepage
from lists.models import Item


class ListsPageTest(TestCase):
    def discard_csrf(self, html_string):
        import re
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', html_string)

# Can be replaced by test_home_page_renders_home_template and test_home_page_uses_item_form
    def test_lists_page_renders_lists_home_template(self):
        response = self.client.get('/lists/new')
        self.assertTemplateUsed(response, 'lists/home.html')

# Can be replaced by test_home_page_renders_home_template and test_home_page_uses_item_form
    def test_lists_page_returns_correct_html(self):
        request = HttpRequest()
        response = lists_homepage(request)

        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        expected_html = self.discard_csrf(render_to_string('lists/home.html'))
        response_html = self.discard_csrf(response.content.decode())
        self.assertEqual(response_html, expected_html)

#         expected_html = render_to_string('home.html', {'form': ItemForm()})
#         self.assertMultiLineEqual(response.content.decode(), expected_html)

# Split this long test case into two:
# 1.def test_home_page_can_save_a_POST_request(self)
# 2.def test_home_page_can_redirects_after_POST(self)
#     def test_home_page_can_save_a_POST_request(self):
#         request = HttpRequest()
#         request.method = 'POST'
#         request.POST['item_text'] = 'A new list item'
#
#         response = lists_homepage(request)
#         self.assertIn('A new list item', response.content.decode(),
#                       'Actual Response is:'+response.content.decode())
#
#         expected_html = self.discard_csrf(render_to_string('lists/home.html',
#                                          {'new_item_text': 'A new list item'}))
#         response_html = self.discard_csrf(response.content.decode())
#         self.assertEqual(response_html, expected_html)
#
#         self.assertEqual(Item.objects.count(), 1)
#         new_item = Item.objects.first()
#         self.assertEqual(new_item.text, 'A new list item')
#
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response['location'], '/')

    def test_lists_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = lists_homepage(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_lists_page_can_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = lists_homepage(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

    def test_lists_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        lists_homepage(request)
        self.assertEqual(Item.objects.count(), 0)

    # discard this TC due to the same function has been covered
    # by ListViewTest:test_lists_displays_all_list_items()
    # def test_lists_page_displays_all_list_items(self):
    #     Item.objects.create(text='itemey 1')
    #     Item.objects.create(text='itemey 2')
    #
    #     request = HttpRequest()
    #     response = lists_homepage(request)
    #
    #     self.assertIn('itemey 1', response.content.decode())
    #     self.assertIn('itemey 2', response.content.decode())


class ListViewTest(TestCase):
    def test_lists_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_lists_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
