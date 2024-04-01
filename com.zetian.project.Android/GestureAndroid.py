# 开发人员：泽天

# 开发时间：2024/3/22 14:54

# 项目定义：
from appium.webdriver.common.appiumby import AppiumBy


class GestureOperation:

    def swipe(self, driver, direction):
        return driver.execute_script("mobile: swipe", {"direction": direction})

    def find_element_by_xpath(self, driver, xpath):
        return driver.find_element(AppiumBy.XPATH, xpath)

    def find_element_by_name(self, driver, name):
        return driver.find_element(AppiumBy.NAME, value=name)

    def flick(self, driver, start_x, start_y, end_x, end_y):
        return driver.flick(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)

    def input_text(self, driver, xpath, text):
        return driver.find_element(AppiumBy.XPATH, xpath).clear().send_keys(text)
