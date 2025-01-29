from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
home = driver.find_element(By.XPATH, "//a/img[@alt='Website for automation practice']")
if home.is_displayed():
    print('Home page is visible')
else:
    print("Home is not visible")