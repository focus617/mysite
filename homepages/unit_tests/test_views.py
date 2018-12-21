#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from unittest import skip

# Create your tests here.
from homepages.views import home_page


class HomePageTest(TestCase):
    maxDiff = None

# Can be replaced by test_home_page_renders_home_template and
# test_home_page_uses_item_form
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepages/index.html')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('homepages/index.html')
        self.assertMultiLineEqual(response.content.decode(), expected_html)


class DateTimeTest(TestCase):

    def test_page_renders_datetime_template(self):
        response = self.client.get('/index/datetime')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepages/datetime.html')

    # def test_passes_correct_offset_to_template(self):
    #     response = self.client.get('/books/datetime/8/')
    #     now = datetime.datetime.now() + datetime.timedelta(hours=8)
        # response.find_element_by_id('local_date_time')
        #self.assertEqual(response.context['local_date_time'], str(now))