#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 9:48
# @File :add_members.py
# @Software :PyCharm
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from appium_ipad.page.base_page import BasePage


class AddMembers(BasePage):
    # def __init__(self, driver):
    #     self._driver = driver

    def manual_input_add(self):
        from appium_ipad.page.manual_input_add import ManualInputAdd
        self.find(By.XPATH, "//*[@text='手动输入添加']").click()
        return ManualInputAdd(self._driver)

    def get_toast(self):
        return self.find(MobileBy.XPATH, "//*[@class = 'android.widget.Toast']").text
