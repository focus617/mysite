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


class SmokeTest(TestCase):
    def test_good_maths(self):
        self.assertEquals(1+1, 2)

    def test_lists_page_renders_lists_home_template(self):
        response = self.client.get('/lists/')
        self.assertTemplateUsed(response, 'lists/home.html')

