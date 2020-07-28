"""
新增信息页面PO
"""
from base.base_page import BasePage
import page


class AddMsgPage(BasePage):
    input_recv = page.input_recv
    input_contents = page.input_contents
    send_btn = page.send_btn

    def recv_user(self, text):
        # 输入接收人
        self.input_func(self.input_recv, text)

    def send_content(self, text):
        # 输入内容
        self.input_func(self.input_contents, text)

    def sent_msg_btn(self):
        # 点击发送按钮
        self.click_func(self.send_btn)
