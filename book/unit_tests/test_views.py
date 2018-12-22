#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from unittest import skip

# Create your tests here.
from book.views import  books_list
from book.models import Classfication, Author, Publisher, Book

class ListsPageTest(TestCase):

    def test_books_list_page_renders_lists_correct_template(self):
        response = self.client.get('/book/books')
        self.assertTemplateUsed(response, 'book/book_list.html')

# Can be replaced by test_home_page_renders_home_template and test_home_page_uses_item_form
    def test_books_list_page_returns_correct_html(self):
        request = HttpRequest()
        response = books_list(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'),  'Response content starts with :' + str(response.content[:10]))
        self.assertIn(b'<title>Web Application</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))


# class NewListTest(TestCase):
#
#     def test_saving_a_POST_request(self):
#         #request = HttpRequest()
#         #request.method = 'POST'
#         #request.POST['text'] = 'A new list item'
#         #response = home_page(request)
#         self.client.post(
#             '/lists/new',
#             data={'text': 'A new list item'}
#         )
#         self.assertEqual(Item.objects.count(), 1)
#         new_item = Item.objects.first()
#         self.assertEqual(new_item.text, 'A new list item')
#
#     def test_redirects_after_POST(self):
#         #request = HttpRequest()
#         #request.method = 'POST'
#         #request.POST['text'] = 'A new list item'
#         #response = home_page(request)
#         response = self.client.post(
#             '/lists/new',
#             data={'text': 'A new list item'}
#         )
#         #self.assertEqual(response.status_code, 302)
#         # self.assertEqual(
#         #    response['location'], '/lists/the-only-list-in-the-world/')
# #         self.assertRedirects(
# #             response, '/lists/the-only-list-in-the-world/')
#         new_list = List.objects.first()
#         self.assertRedirects(
#             response, '/lists/%d/' % (new_list.id,))
#
# # Break down the TC into below 3 TCs
# #     def test_validation_errors_are_sent_back_to_home_page_template(self):
# #         response = self.client.post('/lists/new', data={'text': ''})
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'home.html')
# #         expected_error = escape("You can't have an empty list item")
# #         self.assertContains(response, expected_error)
#
#     def test_for_invalid_input_renders_home_template(self):
#         response = self.client.post('/lists/new', data={'text': ''})
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home.html')
#
#     def test_validation_errors_are_shown_on_home_page(self):
#         response = self.client.post('/lists/new', data={'text': ''})
#         self.assertContains(response, escape(EMPTY_LIST_ERROR))
#
#     def test_for_invalid_input_passes_form_to_template(self):
#         response = self.client.post('/lists/new', data={'text': ''})
#         self.assertIsInstance(response.context['form'], ItemForm)
#
#     def test_invalid_list_items_arent_saved(self):
#         self.client.post('/lists/new', data={'text': ''})
#         self.assertEqual(List.objects.count(), 0)
#         self.assertEqual(Item.objects.count(), 0)
#
#
# class ListViewTest(TestCase):
#
#     def test_uses_list_template(self):
#         #         response = self.client.get('/lists/the-only-list-in-the-world/')
#         list_ = List.objects.create()
#         # 使用Django 测试客户端
#         response = self.client.get('/lists/%d/' % (list_.id,))
#         # 检查使用的模板。然后在模板的上下文中检查各个待办事项
#         self.assertTemplateUsed(response, 'list.html')
#
#     def test_passes_correct_list_to_template(self):
#         other_list = List.objects.create()
#         correct_list = List.objects.create()
#         response = self.client.get('/lists/%d/' % (correct_list.id,))
#         # 检查每个对象都是希望得到的，或者查询集合中包含正确的待办事项
#         self.assertEqual(response.context['list'], correct_list)
#
#     def test_displays_item_form(self):
#         list_ = List.objects.create()
#         response = self.client.get('/lists/%d/' % (list_.id,))
#         # 检查表单使用正确的类
#         self.assertIsInstance(response.context['form'], ExistingListItemForm)
#         self.assertContains(response, 'name="text"')
#
#
# #     def test_list_page_displays_all_list_items(self):
# #         list_ = List.objects.create()
# #         Item.objects.create(text='itemey 1', list=list_)
# #         Item.objects.create(text='itemey 2', list=list_)
# #
# #         response = self.client.get('/lists/the-only-list-in-the-world/')
# #
# #         self.assertContains(response, 'itemey 1')
# #         self.assertContains(response, 'itemey 2')
#
#     def test_list_page_displays_only_items_for_that_list(self):
#         correct_list = List.objects.create()
#         Item.objects.create(text='itemey 1', list=correct_list)
#         Item.objects.create(text='itemey 2', list=correct_list)
#
#         other_list = List.objects.create()
#         Item.objects.create(text='other list item 1', list=other_list)
#         Item.objects.create(text='other list item 2', list=other_list)
#
#         response = self.client.get('/lists/%d/' % (correct_list.id,))
#
#         # 检查模板逻辑：每个for 和if 语句都要做最简单的测试。
#         self.assertContains(response, 'itemey 1')
#         self.assertContains(response, 'itemey 2')
#         self.assertNotContains(response, 'other list item 1')
#         self.assertNotContains(response, 'other list item 2')
#
#     def test_list_page_can_fill_with_data_from_view(self):
#         list_ = List.objects.create()
#         Item.objects.create(text='itemey 1', list=list_)
#         items = Item.objects.all()
#         expected_html = render_to_string(
#             'list.html',
#             {'list': list_}
#         )
#         self.assertIn('itemey 1', expected_html)
#
#     def test_can_save_a_POST_request_to_an_existing_list(self):
#         other_list = List.objects.create()
#         correct_list = List.objects.create()
#
#         self.client.post(
#             '/lists/%d/' % (correct_list.id,),
#             data={'text': 'A new item for an existing list'}
#         )
#
#         # 对于处理POST 请求的视图，确保有效和无效两种情况都要测试
#         self.assertEqual(Item.objects.count(), 1)
#         new_item = Item.objects.first()
#         self.assertEqual(new_item.text, 'A new item for an existing list')
#         self.assertEqual(new_item.list, correct_list)
#
#     def test_POST_redirects_to_list_view(self):
#         other_list = List.objects.create()
#         correct_list = List.objects.create()
#
#         response = self.client.post(
#             '/lists/%d/' % (correct_list.id,),
#             data={'text': 'A new item for an existing list'}
#         )
#         self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))
#
# # Break down into 4 TCs
# #     def test_validation_errors_end_up_on_lists_page(self):
# #         list_ = List.objects.create()
# #         response = self.client.post(
# #             '/lists/%d/' % (list_.id,),
# #             data={'text': ''}
# #         )
# #
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTemplateUsed(response, 'list.html')
# #         self.assertContains(response, escape(EMPTY_LIST_ERROR))
#
# # 对于处理POST 请求的视图，确保有效和无效两种情况都要测试
#     def post_invalid_input(self):
#         list_ = List.objects.create()
#         return self.client.post(
#             '/lists/%d/' % (list_.id,),
#             data={'text': ''}
#         )
#
#     def test_for_invalid_input_nothing_saved_to_db(self):
#         self.post_invalid_input()
#         self.assertEqual(Item.objects.count(), 0)
#
#     def test_for_invalid_input_renders_list_template(self):
#         response = self.post_invalid_input()
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'list.html')
#
# # 健全性检查，检查是否渲染指定的表单，而且是否显示错误消息
#     def test_for_invalid_input_passes_form_to_template(self):
#         response = self.post_invalid_input()
#         self.assertIsInstance(response.context['form'], ExistingListItemForm)
#
#     def test_for_invalid_input_shows_error_on_page(self):
#         response = self.post_invalid_input()
#         self.assertContains(response, escape(EMPTY_LIST_ERROR))
#
#     def test_duplicate_item_validation_errors_end_up_on_lists_page(self):
#         list1 = List.objects.create()
#         item1 = Item.objects.create(list=list1, text='textey')
#
#         response = self.client.post(
#             '/lists/%d/' % (list1.id,),
#             data={'text': 'textey'}
#         )
#
#         expected_error = escape("You've already got this in your list")
#         self.assertContains(response, expected_error)
#         self.assertTemplateUsed(response, 'list.html')
#         self.assertEqual(Item.objects.all().count(), 1)
