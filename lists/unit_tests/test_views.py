#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from unittest import skip

# Create your tests here.
from lists.views import home_page


class HomePageTest(TestCase):

# Can be replaced by test_home_page_renders_home_template and test_home_page_uses_item_form
    def test_lists_page_renders_lists_home_template(self):
        response = self.client.get('/lists/new')
        self.assertTemplateUsed(response, 'lists/home.html')

# Can be replaced by test_home_page_renders_home_template and test_home_page_uses_item_form
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'),  'Response content starts with :' + str(response.content[:10]))
        self.assertIn(b'<title>To-Do Lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
#         expected_html = render_to_string('home.html', {'form': ItemForm()})
#         self.assertMultiLineEqual(response.content.decode(), expected_html)