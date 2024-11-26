# 开发人员：泽天

# 开发时间：2023/11/14 10:52

# 项目定义：
import sys
from appium.webdriver.common.touch_action import TouchAction
from JudgmentLogic.Sleep.SleepTimePrint import sleep
from JudgmentElement.MobileConnection import AppiumSession
from appium.webdriver.common.appiumby import AppiumBy
from OperateLogic.GesturOperation import GestureOperation


class Demo:
    appium_session = AppiumSession(server_url='http://localhost:4723/wd/hub')
    driver = appium_session.start_ios_session(platform_version='16.1', device_name='iPhone 12',
                                              app='com.withyou.bok.app',
                                              udid='00008101-00050C410268001E')
    try:
        sleep(5)
        element = driver.find_element(AppiumBy.XPATH, '//*[@name="PROGRESS"]')
        print("识别到了未读标识")
    except Exception as e:
        print("暂未识别到未读标识，需要检查链接/页面是否包含该元素")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # 打印堆栈跟踪
        print(exc_traceback.tb_lineno)
        print(exc_traceback.tb_next.tb_frame.f_locals)
        print("-" * 90)
        print(e)
    gesture_operation = GestureOperation()

    # 模仿手势滑动
    print("执行向下，向上的滑动")
    gesture_operation.swipe(driver, "up")
    gesture_operation.swipe(driver, "down")
    gesture_operation.find_element_by_xpath(driver, '//*[@name="PROGRESS"]').click()

    # 定位到对应的元素并且点击Menu
    print("点击左上角按钮")
    gesture_operation.find_element_by_xpath(driver, '//*[@name="PROGRESS"]').click()
    print("执行一个向上的滑动，然后执行向左滑动退出当前页面")
    gesture_operation.swipe(driver, "up")
    gesture_operation.swipe(driver, "left")
    # # feed页面
    print("点击底部feed button")
    gesture_operation.find_element_by_xpath(driver, '//*[@name="Feed"]').click()
    print("执行向上和向下的操作，检查页面是否可正常滑动")
    gesture_operation.swipe(driver, "up")
    gesture_operation.swipe(driver, "down")
    # # Explore和FollowTAB切换
    print("切换到Follow TAB")
    gesture_operation.find_element_by_xpath(driver, '//*[@name="Follow"]').click()
    print("执行向上和向下的操作")
    gesture_operation.swipe(driver, "up")
    gesture_operation.swipe(driver, "down")

    # # 中间TAB
    count = 3
    elements = gesture_operation.find_element_by_xpath(driver, '//*[@name="common patriarch female emoji"]')
    for _ in range(3):
        actions = TouchAction(driver)
        actions.press(elements).release().perform()
    # gesture_operation.find_element_by_xpath(driver, '//*[@name="common patriarch female emoji"]').click()
    # # driver.find_element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`value == "0"`]')
    # # 定义一个start像素位置和一个end像素点，控制start到end滑动
    gesture_operation.flick(driver, 53, 364, 141, 371)
    gesture_operation.flick(driver, 318, 367, 219, 363)
    sleep(3)

    # 返回主页
    gesture_operation.find_element_by_xpath(driver, '//*[@name="Home"]').click()

    # 右上角操作
    try:
        elements = driver.find_element(AppiumBy.XPATH, '//*[@name="1"]')
        print("识别到了未读标识")
    except Exception as e:
        print("暂未识别到未读标识，需要检查s链接/页面是否包含该元素")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # 打印堆栈跟踪
        print(exc_traceback.tb_lineno)
        print(exc_traceback.tb_next.tb_frame.f_locals)
        print("-" * 90)
        print(e)

    driver.find_element(AppiumBy.XPATH, '//*[@name="msg"]').click()
    # driver.flick(81, 653, 254, 114)
    driver.find_element(AppiumBy.XPATH, '//*[@name="common black back"]').click()
    driver.execute_script("mobile:swipe", {"direction": "down"})
    sleep(51)
    driver.quit()
