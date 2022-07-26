#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 9:42
# @File :mian.py
# @Software :PyCharm
from selenium.webdriver.common.by import By

from appium_ipad.page.address_list import AddressList


class Main:
    def __init__(self, driver):
        self._driver = driver

    def goto_mail(self):
        pass

    def goto_address_list(self):
        # self._driver(By.XPATH, "//*[@text='通讯录']").click()
        return AddressList(self._driver)