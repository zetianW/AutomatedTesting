# 开发人员：泽天

# 开发时间：2023/11/16 14:58

# 项目定义：
import sys

import appium
from appium.webdriver.common.touch_action import TouchAction
from JudgmentLogic.Sleep.SleepTimePrint import sleep
from JudgmentElement.MobileConnection import AppiumSession
from appium.webdriver.common.appiumby import AppiumBy
from OperateLogic.GesturOperation import GestureOperation


class DemoFile:
    appium_session = AppiumSession(server_url='http://localhost:4723/wd/hub')
    driver = appium_session.start_ios_session(platform_version='16.7.2', device_name='iPhone X',
                                              app='com.itcast.HMiOSTest',
                                              udid='945748259a6c6064b21cd4b5688ba2243720cbe1')
    gesture_operation = GestureOperation()

    # 模仿手势滑动
    print("启动APP成功")
    print("2秒倒计时后点击进入'进入列表'")
    sleep(2)
    gesture_operation.find_element_by_xpath(driver, "//*[@name='进入列表']").click()
    print("倒计时2秒后进行上滑操作")
    sleep(2)
    gesture_operation.swipe(driver, "up")
    print("倒计时2秒后进行下滑操作")
    sleep(2)
    gesture_operation.swipe(driver, "down")
    print("倒计2秒后点击进入6列")
    sleep(2)
    print("倒计2秒后清除输入的文字并且输入huadong.BOK")
    sleep(2)
    gesture_operation.find_element_by_xpath(driver, "//*[@name='6']").click()
    # test_box_element = driver.find_element(AppiumBy.XPATH, "//*[@value='你点进来了第6个选项的界面']").clear().send_keys(
    #     "huadong.BOK")
    gesture_operation.input_text(driver, "//*[@value='你点进来了第6个选项的界面']", "huadong.BOK")
    print("倒计时2秒后点击back返回上一层")
    sleep(2)
    gesture_operation.find_element_by_xpath(driver, "//*[@name='Back']").click()
    print("退出程序，完成Demo执行")
    driver.quit()
