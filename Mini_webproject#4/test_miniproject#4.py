import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_Project3():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    driver.find_element(By.ID,"btn-make-appointment").click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.find_element(By.ID,"txt-username").send_keys("John Doe")
    driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID,"btn-login").click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    appointment_text=driver.find_element(By.TAG_NAME,"h2")
    assert appointment_text.text == "Make Appointment"
