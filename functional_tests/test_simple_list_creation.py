#!/usr/bin/env python
# -*- coding:gbk -*-

from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# class NewVisitorTest(unittest.TestCase):
# class NewVisitorTest(LiveServerTestCase):


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # ����˿��˵��һ���ܿ�����ߴ�������Ӧ��
        # ��ȥ�������Ӧ�õ���ҳ
        #    self.browser.get('http://localhost:8000')
        self.browser.get(self.server_url + '/lists/new')
    # ��ע�⵽��ҳ�ı����ͷ����������To-Do�������
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

    # Ӧ������������һ����������
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
    # ����һ���ı����������ˡ�Buy peacock feathers���������ȸ��ë��
    # ����˿�İ�����ʹ�ü�Ӭ��������
        inputbox.send_keys('Buy peacock feathers')

    # �����س����󣬱�������һ����URL
    # ���ҳ��Ĵ�������������ʾ�ˡ�1: Buy peacock feathers��
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

    # ҳ��������ʾ��һ���ı��򣬿������������Ĵ�������
    # �������ˡ�Use peacock feathers to make a fly����ʹ�ÿ�ȸ��ë����Ӭ��
    # ����˿���º�������
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    # ҳ���ٴθ��£������嵥����ʾ����������������
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly')
    # ����˿��֪�������վ�Ƿ���ס�����嵥
    # ��������վΪ��������һ��Ψһ��URL
    # ����ҳ������һЩ���ֽ�˵�������
    # �������Ǹ�URL���������Ĵ��������б���
    # �������⣬ȥ˯����

    # ����һ������������˹�����û���������վ
    # # ����ʹ��һ����������Ự
    # # ȷ������˿����Ϣ�����cookie��й¶����
        self.browser.quit()
        self.browser = webdriver.Firefox()
    # ������˹������ҳ
    # ҳ���п���������˿���嵥
        self.browser.get(self.server_url + '/lists/new')
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
    # ������˹����һ���´�������½�һ���嵥
    # ����������˿������Ȥ��Ȼ
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
    # ������˹���������ΨһURL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
    # ���ҳ�滹��û������˿���嵥
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
    # ���˶������⣬ȥ˯����


# if __name__ == '__main__':
#  unittest.main(warnings='ignore')
