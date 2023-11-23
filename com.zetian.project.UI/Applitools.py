# 开发人员：泽天

# 开发时间：2023/11/21 16:10

# 项目定义：
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver
from applitools.selenium.eyes import Eyes


class HelloWorld:
    # Initialize the eyes SDK and set your private API key.
    eyes = Eyes()
    eyes.api_key = 'keyY1lvi8USbQ36jPCtM5e5BmZAilnFB4b4D103LY3LZQ110'

    # Set the desired capapbilities, be sure to change the values accordingly
    desired_caps = {}
    desired_caps['platformName'] = 'iOS'
    desired_caps['browserName'] = 'Safari'
    desired_caps['deviceName'] = 'iphone 12'
    desired_caps['platformVersion'] = '16.1'
    desired_caps['automationName'] = 'XCUITest'

    # Open browser
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    try:

        # Start the test.
        eyes.open(driver=driver, app_name='Hello World!', test_name='My first Appium web Python test!')

        # Navigate the browser to the "Hello World!" web-site.
        driver.get(r'https://applitools.com/helloworld')

        # Visual validation point #1.
        eyes.check_window('Hello!')

        # Click the "Click me!" button.
        driver.find_element(AppiumBy.XPATH, '//*[@name="button"]').click()

        # Visual validation #2.
        eyes.check_window('Click!')

        # End the test.
        eyes.close()

    finally:

        # Close the browser.
        driver.quit()

        # If the test was aborted before eyes.Close was called, end the test as aborted.
        eyes.abort_if_not_closed()
