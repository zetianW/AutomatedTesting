# 开发人员：泽天

# 开发时间：2023/11/21 11:08

# 项目定义：
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from JudgmentElement.MobileConnection import AppiumSession
from appium.webdriver.common.touch_action import TouchAction
from JudgmentLogic.Sleep.SleepTimePrint import sleep
from JudgmentElement.MobileConnection import AppiumSession
from appium.webdriver.common.appiumby import AppiumBy
from OperateLogic.GesturOperation import GestureOperation
from appium.webdriver.common.mobileby import MobileBy


class JingDong:
    appium_session = AppiumSession(server_url='http://localhost:4723/wd/hub')
    driver = appium_session.start_ios_session(platform_version='16.7.2', device_name='iPhone X',
                                              app='com.360buy.jdmobile',
                                              udid='00008101-00050C410268001E')

    gesture_operation = GestureOperation()
    # wait = WebDriverWait(driver, 60)
    gesture_operation.find_element_by_xpath(driver, '//*[@name="购物车"]').click()
    sleep(2)
    gesture_operation.find_element_by_xpath(driver, '//*[@name="去结算(1)件商品"]').click()
    sleep(2)
    gesture_operation.find_element_by_xpath(driver, '//*[@name="提交订单"]').click()

    gesture_operation.find_element_by_xpath(driver, '//*[@name="确认付款"]').click()
