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
from lists.models import Item, List


class ListsPageTest(TestCase):
    def discard_csrf(self, html_string):
        import re
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex, '', html_string)

# Can be replaced by test_home_page_renders_home_template and test_home_page_uses_item_form
    def test_lists_page_renders_lists_home_template(self):
        response = self.client.get('/lists/')
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

# Split this long test case into two TCs:
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

    # Move to class NewListTest
    # def test_lists_page_can_save_a_POST_request(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = lists_homepage(request)
    #
    #     self.assertEqual(Item.objects.count(), 1)
    #     new_item = Item.objects.first()
    #     self.assertEqual(new_item.text, 'A new list item')
    #
    # Move to class NewListTest
    # def test_lists_page_can_redirects_after_POST(self):
    #     request = HttpRequest()
    #     request.method = 'POST'
    #     request.POST['item_text'] = 'A new list item'
    #
    #     response = lists_homepage(request)
    #
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
    #
    # def test_lists_page_only_saves_items_when_necessary(self):
    #     request = HttpRequest()
    #     lists_homepage(request)
    #     self.assertEqual(Item.objects.count(), 0)

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
        # response = self.client.get('/lists/the-only-list-in-the-world/')
        # self.assertTemplateUsed(response, 'lists/list.html')
        list_ = List.objects.create()
        # 使用Django 测试客户端
        response = self.client.get('/lists/%d/' % (list_.id,))
        # 检查使用的模板。然后在模板的上下文中检查各个待办事项
        self.assertTemplateUsed(response, 'lists/list.html')

    # Refactor to test_list_page_displays_only_items_for_that_list() due to introduce Item.list
    # def test_lists_displays_all_list_items(self):
    #     list_ = List.objects.create()
    #     Item.objects.create(text='itemey 1', list=list_)
    #     Item.objects.create(text='itemey 2', list=list_)
    #
    #     response = self.client.get('/lists/the-only-list-in-the-world/')
    #
    #     self.assertContains(response, 'itemey 1')
    #     self.assertContains(response, 'itemey 2')
    def test_list_page_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)

        response = self.client.get('/lists/%d/' % (correct_list.id,))

        # 检查模板逻辑：每个for 和if 语句都要做最简单的测试。
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')


class NewListTest(TestCase):

    def test_lists_page_can_save_a_POST_request(self):
        # Refactor below statement with TestCase.client
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = 'A new list item'
        # response = lists_homepage(request)
        self.client.post('/lists/new',
                         data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_lists_page_can_redirects_after_POST(self):
        # Refactor below statement with TestCase.client
        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = 'A new list item'
        # response = lists_homepage(request)
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        # 上面曾经遇到404（找不到网页）问题，困扰了很久。最后问题出在URL地址上self.client.post('lists/new'...
        # 漏写了一个/

        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')

        # Refactor due to introduce Item.list
        # self.assertRedirects(response, '/lists/the-only-list-in-the-world/')

        new_list = List.objects.first()
        self.assertRedirects(response, '/lists/%d/' % new_list.id)

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'item_text': 'A new item for an existing list'}
        )

        # 对于处理POST 请求的视图，确保有效和无效两种情况都要测试
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_POST_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'item_text': 'A new item for an existing list'}
        )
        self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))

        # 检查每个对象都是希望得到的，或者查询集合中包含正确的待办事项
        self.assertEqual(response.context['list'], correct_list)

# Break down the TC into below 3 TCs
    def test_validation_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/home.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)

    def test_invalid_list_items_arent_saved(self):
        self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)
