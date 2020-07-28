"""
获取所有po页面类对象方法
"""
from page.addmsg_page import AddMsgPage
from page.message_page import MessagePage


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def information_page(self):
        return MessagePage(self.driver)

    @property
    def add_page(self):
        return AddMsgPage(self.driver)
