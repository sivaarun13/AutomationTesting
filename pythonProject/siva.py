from selenium import webdriver
from selenium.webdriver import chrome
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


username = "arunchinni9999@gmail.com"
password = "Sivaarun1911211351"

driver = webdriver.Chrome()
time.sleep(5)
driver.get('https://www.gmail.com')
time.sleep(2)
driver.find_element(By.ID, "identifierId").send_keys(username)
time.sleep(5)
driver.find_element(By.ID, "identifierNext").click()
time.sleep(5)
driver.find_element(By.ID, "password").send_keys(password)
time.sleep(5)
driver.find_element(By.ID, "passwordNext").click()
time.sleep(10)

