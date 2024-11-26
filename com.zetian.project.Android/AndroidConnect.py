# 开发人员：泽天

# 开发时间：2024/3/22 13:58

# 项目定义：
import os
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from GestureAndroid import GestureOperation

# 设定Appium服务器URL
server_url = 'http://localhost:4723/wd/hub'

# 设定Desired Capabilities
desired_caps= {
    'automationName': 'UIAutomator2',
    'platformName': 'Android',
    'deviceName': 'Galaxy S20 5G',
    'platformVersion': '13',
    'appPackage': 'com.huadongmeta.bok',
    'appActivity': 'com.huadongmeta.bok.splash.SplashActivity'}

# 创建Appium会话
driver = webdriver.Remote(server_url,desired_caps)
try:
    wait = WebDriverWait(driver, 10)
    # 指定截图保存的目录
    save_dir = '/Users/edy/Desktop/3月26日'

    # 循环截屏并保存
    for i in range(2):  # 例如循环10次，即每隔5秒截取10次屏幕
        time.sleep(5)  # 暂停5秒
        screenshot = driver.get_screenshot_as_png()

        with open(os.path.join(save_dir, f'screenshot_{i}.png'), 'wb') as file:
            file.write(screenshot)
    element = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//*[@resource-id="com.huadongmeta.bok:id/iv_qa"]')))
    print("指定元素加载完成")

except Exception as e:
    print(f"没有找到指定元素+{e}")
finally:
    time.sleep(10)
