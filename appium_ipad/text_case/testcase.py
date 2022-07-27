#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 16:00
# @File :testcase.py
# @Software :PyCharm
from appium_ipad.page.app import App


class TestCase:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        invitpage = self.main.goto_address_list().goto_add_members().manual_input_add().complete_input().input_name().\
            input_phone().inpout_mail().click_save()
        assert '成功' in invitpage.get_toast()
