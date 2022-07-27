#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/27 0027 14:13
# @File :base_page.py
# @Software :PyCharm
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [
        (By.XPATH, "//*[@text = '确认']"),
        (By.XPATH, "//*[@text = '下次再说']"),
        (By.XPATH, "//*[@text = '确定']"),
    ]
    _err_num = 0
    _max_num = 3

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        element: WebElement
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            self._err_num = 0
            self._driver.implicitly_wait(20)
            return element
        except Exception as e:
            self._driver.implicitly_wait(5)
            if self._err_num > self._max_num:
                raise e
            self._err_num += 1
            for ele in self._black_list:
                elelist = self._driver.find_element(*ele)
                if len(elelist) > 0:
                    elelist.click()
                    return self.find(locator, value)
