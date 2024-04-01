# 开发人员：泽天

# 开发时间：2023/11/14 10:02

# 项目定义：使用Try...Except判断页面是否存在该元素

from appium import webdriver


class AppiumSession:
    # 调用Appium服务端口
    def __init__(self, server_url='http://localhost:4723/wd/hub'):
        self.driver = None
        self.server_url = server_url

    # 启动IOS服务的协议（也就是代码中需要针对于连接的要测试的真机进行设定）
    def start_ios_session(self, platform_version=None, device_name=None, app=None, udid=None):
        desired_caps = {'platformName': 'iOS',
                        'platformVersion': platform_version,
                        'deviceName': device_name,
                        'app': app}
        if udid:
            desired_caps['udid'] = udid
        if platform_version:
            desired_caps['platfossrm_version'] = platform_version
        if device_name:
            desired_caps['device_name'] = device_name
        elif app:
            desired_caps['app'] = app

        self.driver = webdriver.Remote(self.server_url, desired_caps)
        return self.driver
