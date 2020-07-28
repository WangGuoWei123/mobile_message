"""
短信页面po
"""
from base.base_page import BasePage
import page


class MessagePage(BasePage):
    add_btn = page.add_btn

    def click_add_message(self):
        self.click_func(self.add_btn)
