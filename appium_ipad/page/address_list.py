#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 9:47
# @File :address_list.py
# @Software :PyCharm
from appium_ipad.page.add_members import AddMembers


class AddressList:
    def __init__(self, driver):
        self._driver = driver

    def goto_add_members(self):
        return AddMembers(self._driver)