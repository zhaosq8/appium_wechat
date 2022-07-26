#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Author :zhaosq
# @Time :2022/7/26 0026 9:38
# @File :app.py
# @Software :PyCharm
from appium_ipad.page.mian import Main


class App:
    def start(self):
        return self

    def stop(self):
        pass

    def restart(self):
        pass

    def main(self) -> Main:
        return Main()