#!/usr/bin/env python
# -*- coding:gbk -*-

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape
from unittest import skip

# Create your tests here.
from lists.views import home_page
from lists.models import Item, List
from lists.forms import ItemForm, ExistingListItemForm, EMPTY_LIST_ERROR, DUPLICATE_ITEM_ERROR


class HomePageTest(TestCase):
    maxDiff = None

# Can be replaced by test_home_page_renders_home_template and test_home_page_uses_item_form
#     def test_root_url_resolves_to_home_page_view(self):
#         found = resolve('/')
#         self.assertEqual(found.func, home_page)

# Can be replaced by test_home_page_renders_home_template and test_home_page_uses_item_form
#     def test_home_page_returns_correct_html(self):
#         request = HttpRequest()
#         response = home_page(request)
#         self.assertTrue(response.content.startswith(b'<html'))
#         self.assertIn(b'<title>To-Do Lists</title>', response.content)
#         self.assertTrue(response.content.strip().endswith(b'</html>'))
# #         expected_html = render_to_string('home.html', {'form': ItemForm()})
# #         self.assertMultiLineEqual(response.content.decode(), expected_html)

    def test_home_page_renders_home_template(self):
        response = self.client.get('/lists/new')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_uses_item_form(self):
        response = self.client.get('/lists/new')
        self.assertIsInstance(response.context['form'], ItemForm)

    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)

# Remove this TC:  since we need upgrade to DB for multi-user
#     def test_home_page_displays_all_list_items(self):
#         Item.objects.create(text='itemey 1')
#         Item.objects.create(text='itemey 2')
#
#         request = HttpRequest()
#         response = home_page(request)
#
#         self.assertIn('itemey 1', response.content.decode())
#         self.assertIn('itemey 2', response.content.decode())

# Move this TC to new class "NewListTest":
#     def test_home_page_can_save_a_POST_request(self):
#         request = HttpRequest()
#         request.method = 'POST'
#         request.POST['text'] = 'A new list item'
#
#         response = home_page(request)
#
#         self.assertEqual(Item.objects.count(), 1)
#         new_item = Item.objects.first()
#         self.assertEqual(new_item.text, 'A new list item')

# Move this TC to new class "NewListTest":
#     def test_home_page_can_redirects_after_POST(self):
#         request = HttpRequest()
#         request.method = 'POST'
#         request.POST['text'] = 'A new list item'
#
#         response = home_page(request)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')


class NewListTest(TestCase):

    def test_saving_a_POST_request(self):
        #request = HttpRequest()
        #request.method = 'POST'
        #request.POST['text'] = 'A new list item'
        #response = home_page(request)
        self.client.post(
            '/lists/new',
            data={'text': 'A new list item'}
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        #request = HttpRequest()
        #request.method = 'POST'
        #request.POST['text'] = 'A new list item'
        #response = home_page(request)
        response = self.client.post(
            '/lists/new',
            data={'text': 'A new list item'}
        )
        #self.assertEqual(response.status_code, 302)
        # self.assertEqual(
        #    response['location'], '/lists/the-only-list-in-the-world/')
#         self.assertRedirects(
#             response, '/lists/the-only-list-in-the-world/')
        new_list = List.objects.first()
        self.assertRedirects(
            response, '/lists/%d/' % (new_list.id,))

# Break down the TC into below 3 TCs
#     def test_validation_errors_are_sent_back_to_home_page_template(self):
#         response = self.client.post('/lists/new', data={'text': ''})
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home.html')
#         expected_error = escape("You can't have an empty list item")
#         self.assertContains(response, expected_error)

    def test_for_invalid_input_renders_home_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_validation_errors_are_shown_on_home_page(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertContains(response, escape(EMPTY_LIST_ERROR))

    def test_for_invalid_input_passes_form_to_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertIsInstance(response.context['form'], ItemForm)

    def test_invalid_list_items_arent_saved(self):
        self.client.post('/lists/new', data={'text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        #         response = self.client.get('/lists/the-only-list-in-the-world/')
        list_ = List.objects.create()
        # ʹ��Django ���Կͻ���
        response = self.client.get('/lists/%d/' % (list_.id,))
        # ���ʹ�õ�ģ�塣Ȼ����ģ����������м�������������
        self.assertTemplateUsed(response, 'list.html')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        # ���ÿ��������ϣ���õ��ģ����߲�ѯ�����а�����ȷ�Ĵ�������
        self.assertEqual(response.context['list'], correct_list)

    def test_displays_item_form(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/' % (list_.id,))
        # ����ʹ����ȷ����
        self.assertIsInstance(response.context['form'], ExistingListItemForm)
        self.assertContains(response, 'name="text"')


#     def test_list_page_displays_all_list_items(self):
#         list_ = List.objects.create()
#         Item.objects.create(text='itemey 1', list=list_)
#         Item.objects.create(text='itemey 2', list=list_)
#
#         response = self.client.get('/lists/the-only-list-in-the-world/')
#
#         self.assertContains(response, 'itemey 1')
#         self.assertContains(response, 'itemey 2')

    def test_list_page_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)

        response = self.client.get('/lists/%d/' % (correct_list.id,))

        # ���ģ���߼���ÿ��for ��if ��䶼Ҫ����򵥵Ĳ��ԡ�
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')

    def test_list_page_can_fill_with_data_from_view(self):
        list_ = List.objects.create()
        Item.objects.create(text='itemey 1', list=list_)
        items = Item.objects.all()
        expected_html = render_to_string(
            'list.html',
            {'list': list_}
        )
        self.assertIn('itemey 1', expected_html)

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'text': 'A new item for an existing list'}
        )

        # ���ڴ���POST �������ͼ��ȷ����Ч����Ч���������Ҫ����
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_POST_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'text': 'A new item for an existing list'}
        )
        self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))

# Break down into 4 TCs
#     def test_validation_errors_end_up_on_lists_page(self):
#         list_ = List.objects.create()
#         response = self.client.post(
#             '/lists/%d/' % (list_.id,),
#             data={'text': ''}
#         )
#
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'list.html')
#         self.assertContains(response, escape(EMPTY_LIST_ERROR))

# ���ڴ���POST �������ͼ��ȷ����Ч����Ч���������Ҫ����
    def post_invalid_input(self):
        list_ = List.objects.create()
        return self.client.post(
            '/lists/%d/' % (list_.id,),
            data={'text': ''}
        )

    def test_for_invalid_input_nothing_saved_to_db(self):
        self.post_invalid_input()
        self.assertEqual(Item.objects.count(), 0)

    def test_for_invalid_input_renders_list_template(self):
        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')

# ��ȫ�Լ�飬����Ƿ���Ⱦָ���ı��������Ƿ���ʾ������Ϣ
    def test_for_invalid_input_passes_form_to_template(self):
        response = self.post_invalid_input()
        self.assertIsInstance(response.context['form'], ExistingListItemForm)

    def test_for_invalid_input_shows_error_on_page(self):
        response = self.post_invalid_input()
        self.assertContains(response, escape(EMPTY_LIST_ERROR))

    def test_duplicate_item_validation_errors_end_up_on_lists_page(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='textey')

        response = self.client.post(
            '/lists/%d/' % (list1.id,),
            data={'text': 'textey'}
        )

        expected_error = escape("You've already got this in your list")
        self.assertContains(response, expected_error)
        self.assertTemplateUsed(response, 'list.html')
        self.assertEqual(Item.objects.all().count(), 1)
