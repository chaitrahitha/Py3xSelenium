import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Project3():
    driver=webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    driver.find_element(By.ID,"username").send_keys("augtest_040823@idrive.com")
    driver.find_element(By.ID,"password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
    time.sleep(15)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    upgrade=driver.find_element(By.XPATH,"//span[text()='Your free trial has expired']").text
    assert upgrade == "Your free trial has expired"
    allure.attach(driver.get_screenshot_as_png(), name="error_message-screenshot")