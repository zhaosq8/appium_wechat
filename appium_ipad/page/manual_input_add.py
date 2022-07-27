#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 9:50
# @File :manual_input_add.py
# @Software :PyCharm
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class ManualInputAdd:
    def __init__(self, driver):
        self._driver = driver

    def complete_input(self):
        self._driver.find.element(MobileBy.XPATH, "//*[@text = '完整输入']").click()
        sleep(5)
        return self

    def input_name(self):
        self._driver.find.element(MobileBy.XPATH, "//*[@text = '姓名　']/..//*[@class = 'android.widget.EditText']")\
            .send_keys('李2')
        return self

    def inpout_mail(self):
        self._driver.find.element(By.XPATH, "//*[@text = '企业邮箱　']/..//*[@class = 'android.widget.EditText']").send_keys('4346564')
        return self

    def input_phone(self):
        self._driver.find.element(By.ID, "com.tencent.wework:id/hyw").send_keys('10013211011')
        return self

    def click_save(self):
        from appium_ipad.page.add_members import AddMembers
        x = self._driver.get_window_size()['width']
        y = self._driver.get_window_size()['height']
        x1 = int(x * 0.5)
        x2 = int(x * 0.5)
        y1 = int(y * 0.8)
        y2 = int(y * 0.2)
        self._driver.swipe(x1, y1, x2, y2, 1000)
        self._driver.find.element(By.ID, "com.tencent.wework:id/aw3").click()
        return AddMembers(self._driver)
