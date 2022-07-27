#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 9:47
# @File :address_list.py
# @Software :PyCharm
from selenium.webdriver.common.by import By

from appium_ipad.page.add_members import AddMembers
from appium_ipad.page.base_page import BasePage


class AddressList(BasePage):
    # def __init__(self, driver):
    #     self._driver = driver

    def goto_add_members(self):
        self.find(By.XPATH, "//*[@text='添加成员']").click()
        return AddMembers(self._driver)