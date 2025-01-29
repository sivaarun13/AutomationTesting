from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://automationexercise.com")
home = driver.find_element(By.XPATH, "//a/img[@alt='Website for automation practice']")
if home.is_displayed():
    print('Home page is visible')
else:
    print("Home is not visible")

driver.find_element(By.XPATH, "//a[text()=' Test Cases']").click()
verify = driver.find_element(By.XPATH, "//h2/b")
if verify.is_displayed():
    print("Test Cases is visible")
else:
    print("Test case is not visible")
