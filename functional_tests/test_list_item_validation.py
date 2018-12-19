#!/usr/bin/env python
# -*- coding:gbk -*-

from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time


# class NewVisitorTest(unittest.TestCase):
# class NewVisitorTest(LiveServerTestCase):


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # ����˿������ҳ����С���ύ��һ���մ�������
        # �������û�������ݣ����Ͱ����˻س���
        self.browser.get(self.server_url + '/lists/new')
        inputbox = self.get_item_input_box()

        # self.get_item_input_box().send_keys('\n')
        inputbox.send_keys('\n')

        # ��ҳˢ���ˣ���ʾһ��������Ϣ
        # ��ʾ���������Ϊ��
#         error = self.get_error_element()
#         self.assertEqual(error.text, "You can't have an empty list item")

        # ������һЩ���֣�Ȼ���ٴ��ύ�����û������
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy milk')

        # ���е����Ƥ�����ύ��һ���մ�������
        # self.get_item_input_box().send_keys('\n')
        inputbox = self.get_item_input_box()
        inputbox.send_keys('\n')

        # ���嵥ҳ����������һ�����ƵĴ�����Ϣ
        self.check_for_row_in_list_table('1: Buy milk')
#        error = self.get_error_element()
#        self.assertEqual(error.text, "You can't have an empty list item")

        # ��������֮���û������
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Make tea')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # ����˿������ҳ���½�һ���嵥
        self.browser.get(self.server_url + '/lists/new')
        #self.get_item_input_box().send_keys('Buy milk\n')
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy milk')

        #self.get_item_input_box().send_keys('Buy wellies\n')
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy wellies')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('2: Buy wellies')

        # ����С��������һ���ظ��Ĵ�������
        #self.get_item_input_box().send_keys('Buy wellies\n')
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy wellies')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # ������һ���а����Ĵ�����Ϣ
        self.check_for_row_in_list_table('2: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # ����˿�½�һ���嵥�����������������Գ�����һ����֤����
        self.browser.get(self.server_url + '/lists/new')
        self.get_item_input_box().send_keys('\n')
#         error = self.get_error_element()
#         self.assertTrue(error.is_displayed())

        # Ϊ��������������ʼ�����������������
        inputbox = self.get_item_input_box()
        inputbox.send_keys('a')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # ����������Ϣ��ʧ�ˣ����ܸ���
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())

# if __name__ == '__main__':
#  unittest.main(warnings='ignore')
