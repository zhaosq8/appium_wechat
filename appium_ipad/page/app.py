#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 9:38
# @File :app.py
# @Software :PyCharm
from appium import webdriver

from appium_ipad.page.base_page import BasePage
from appium_ipad.page.mian import Main


class App(BasePage):
    def start(self):
        if self._driver == None:
            caps = {"platformName": "Android",
                    "deviceName": "FJRNW19B14005164",
                    "appPackage": "com.tencent.wework",
                    "appActivity": ".launch.LaunchSplashActivity",
                    # "unicodeKeyboard": "True",
                    # "resetKeyboard": "True",
                    # # 跳过安装
                    # 'skipServerInstallation': True,
                    # # 跳过设备初始化
                    # 'skipDeviceInitialization': True,
                    # 获取toast
                    'automationName': 'uiautomator2',
                    'noRest': True
                    }
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(20)
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
