#!/usr/bin/env python
# -*- coding:gbk -*-

from .base import FunctionalTest

# class NewVisitorTest(unittest.TestCase):
# class NewVisitorTest(LiveServerTestCase):


class NewVisitorTest(FunctionalTest):

    def test_layout_and_styling(self):
        # ����˿������ҳ
        self.browser.get(self.server_url + '/lists/new')
        self.browser.set_window_size(1024, 768)
        # ����������������ؾ�����ʾ
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=250
        )
        # ���½���һ���嵥������������������ؾ�����ʾ
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=250
        )


# if __name__ == '__main__':
#  unittest.main(warnings='ignore')
