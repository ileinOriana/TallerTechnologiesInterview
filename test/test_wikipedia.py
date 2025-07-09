from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

APP_PATH = "/Users/ile/Documents/interview/TestApp-iphonesimulator.app"

options = XCUITestOptions()
options.platform_name = "iOS"
options.platform_version = "18.5"
options.device_name = "iPhone 16"
options.app = APP_PATH
options.no_reset = True
options.automation_name = "XCUITest"

driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    print("Starting test...")

    button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "show alert")
    button.click()

    time.sleep(1)
    alert_ok = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OK")
    assert alert_ok.is_displayed(), "OK button not visible"

    driver.save_screenshot("screenshot.png")
    print("Test Passed - screenshot saved as screenshot.png")

except Exception as e:
    print(f" Test Failed: {e}")

finally:
    driver.quit()