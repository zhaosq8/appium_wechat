#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 9:47
# @File :address_list.py
# @Software :PyCharm
class AddressList:

    def goto_add_members(self):
        from appium_ipad.page.add_members import AddMembers
        return AddMembers()