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


class ListsPageTest(TestCase):

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
        expected_html = render_to_string('lists/home.html')
        self.assertEqual(response.content.decode(), expected_html)

#         expected_html = render_to_string('home.html', {'form': ItemForm()})
#         self.assertMultiLineEqual(response.content.decode(), expected_html)

# Move this TC to new class "NewListTest":
    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = lists_homepage(request)
        self.assertIn('A new list item', response.content.decode())

        expected_html = render_to_string('lists/home.html',
                                         { 'new_item_text': 'A new list item'})
        self.assertEqual(response.content.decode(), expected_html)

        # self.assertEqual(Item.objects.count(), 1)
        # new_item = Item.objects.first()
        # self.assertEqual(new_item.text, 'A new list item')