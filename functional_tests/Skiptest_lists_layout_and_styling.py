#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .lists_base import FunctionalTest

# class NewVisitorTest(unittest.TestCase):
# class NewVisitorTest(LiveServerTestCase):


class NewVisitorTest(FunctionalTest):

    def test_layout_and_styling(self):
        # 伊迪丝访问首页
        self.browser.get(self.server_url + '/lists/new')
        self.browser.set_window_size(1024, 768)
        # 她看到输入框完美地居中显示
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=250
        )
        # 她新建了一个清单，看到输入框仍完美地居中显示
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=250
        )


# if __name__ == '__main__':
#  unittest.main(warnings='ignore')
