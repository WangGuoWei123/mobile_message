from selenium.webdriver.common.by import By

# 信息页面属性
add_btn = By.ID, "com.android.mms:id/action_compose_new"

# 新建页面属性
input_recv = By.XPATH, "//*[contains(@text,'接收者')]"
input_contents = By.XPATH, "//*[contains(@text,'键入信息')]"
send_btn = By.ID, "com.android.mms:id/send_button_sms"
