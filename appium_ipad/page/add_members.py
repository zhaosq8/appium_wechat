#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 9:48
# @File :add_members.py
# @Software :PyCharm
from selenium.webdriver.common.by import By


class AddMembers:
    def __init__(self, driver):
        self._driver = driver

    def manual_input_add(self):
        from appium_ipad.page.manual_input_add import ManualInputAdd
        self._driver.find_element(By.XPATH, "//*[@text='手动输入添加']").click()
        return ManualInputAdd(self._driver)