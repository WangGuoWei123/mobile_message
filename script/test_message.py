import pytest
import allure
from common.utils import make_driver
from page.page import Page
from tools.read_data import read_msg


class TestMassage(object):
    # 设置用例严重级别
    BLOCKER = allure.MASTER_HELPER.severity_level.BLOCKER
    CRITICAL = allure.MASTER_HELPER.severity_level.CRITICAL
    NORMAL = allure.MASTER_HELPER.severity_level.NORMAL
    MINOR = allure.MASTER_HELPER.severity_level.MINOR
    TRIVIAL = allure.MASTER_HELPER.severity_level.TRIVIAL
    driver = None
    page = None

    def setup(self):
        self.driver = make_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # @allure.MASTER_HELPER.severity(allure.MASTER_HELPER.severity_level.TRIVIAL)
    @allure.MASTER_HELPER.severity(BLOCKER)
    @allure.MASTER_HELPER.step(title="发送短信")
    @pytest.mark.parametrize("mobile,content", read_msg())
    def test_send_msg(self, mobile, content):
        allure.MASTER_HELPER.attach("发送短信的步骤", "通过手机号发送短信")
        self.page.information_page.click_add_message()
        self.page.add_page.recv_user(mobile)
        self.page.add_page.send_content(content)
        self.page.add_page.sent_msg_btn()
    

