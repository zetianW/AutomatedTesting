# 开发人员：泽天

# 开发时间：2023/11/21 11:08

# 项目定义：
import datetime
import threading
import time

from JudgmentLogic.Sleep.SleepTimePrint import sleep
from selenium.webdriver.common.action_chains import ActionChains


class GestureOperation:

    def swipe(self, driver, direction):
        return driver.execute_script("mobile: swipe", {"direction": direction})

    def find_element_by_xpath(self, driver, xpath):
        return driver.find_element(AppiumBy.XPATH, xpath)

    def find_element_by_name(self, driver, name):
        return driver.find_element(AppiumBy.NAME, value=name)

    def flick(self, driver, start_x, start_y, end_x, end_y):
        return driver.flick(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)

    def input_text_xpath(self, driver, xpath, text):
        return driver.find_element(AppiumBy.XPATH, xpath).clear().send_keys(text)

    def text_classname(self, driver, class_name):
        return driver.find_element(AppiumBy.CLASS_NAME, class_name)

    def auto_click_at_eight(self):
        timestamp_seconds = datetime.datetime.now()
        return timestamp_seconds


from appium.webdriver.common.appiumby import AppiumBy

from JudgmentElement.MobileConnection import AppiumSession


class JinDong:
    appium_session = AppiumSession(server_url='http://localhost:4723/wd/hub')
    driver = appium_session.start_ios_session(platform_version='16.1', device_name='iPhone 12',
                                              app='com.360buy.jdmobile',
                                              udid='00008101-00050C410268001E')

    # gesture_operation = GestureOperation()
    # target_timestamp = datetime.datetime(2024, 1, 26, 12, 25, 0, 0)
    # while datetime.datetime.now() == target_timestamp:
    #     time.sleep(1)

    gesture_operation = GestureOperation()
    sleep(5)
    gesture_operation.text_classname(driver, 'XCUIElementTypeSearchField').click()
    gesture_operation.text_classname(driver, 'XCUIElementTypeSearchField').clear().send_keys("茅台酒1499元预约")
    gesture_operation.find_element_by_xpath(driver, '//XCUIElementTypeButton[@name="搜索"]').click()
    gesture_operation.find_element_by_xpath(driver, '//*[@name="京东"]').click()
    now = datetime.datetime.now()
    target_time = now.replace(2024, 1, 29, 14, 3, 0, 0)
    if target_time <= now:
        target_time += datetime.timedelta(days=1)
    TOLERANCE_IN_MILLISECONDS = 0.5
    while True:
        current_time = datetime.datetime.now()
        time_difference = (target_time - current_time).total_seconds()
        if abs(time_difference) <= TOLERANCE_IN_MILLISECONDS:
            gesture_operation.flick(driver, 342, 729, 342, 729)
            break
        wait_time = max(time_difference / 1000.0, 0)
        if wait_time == 0:
            gesture_operation.flick(driver, 342, 729, 342, 729)
        time.sleep(wait_time)
