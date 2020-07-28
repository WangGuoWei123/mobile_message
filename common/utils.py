from appium import webdriver


def make_driver():
    # 启动配置参数
    capabilities = {
        "platformName": "Android",  # 平台名称
        "platformVersion": "5.1",  # 手机或者模拟器版本
        "deviceName": "192.168.97.101:5555",  # 手机或者模拟器名字
        "appPackage": "com.android.mms",  # 包名
        "appActivity": ".ui.ConversationList",  # 启动名
        "resetKeyboard": True,  # 重置键盘⼤家可以将输⼊的abc 改成 输⼊中⽂， 得到的结果:输⼊框⽆任何值输⼊且程序不会抱错
        "unicodeKeyboard": True,  # 改变编码方式
        "noReset": True  # 不重置应用状态(比如设备第一次确定之后，在之后的操作不会在提示窗口)
    }
    # 实例化驱动对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver
