"""
基类po页面封装定位点击发送方法
"""
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_func(self, location, timeout=10, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(
            lambda x: x.find_element(location[0], location[1]))

    def click_func(self, location):
        self.find_element_func(location).click()

    def input_func(self, location, text):
        element = self.find_element_func(location)
        element.clear()
        element.send_keys(text)
