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
driver.find_element(By.XPATH, "//a/i[@class='material-icons card_travel']").click()
products = driver.find_element(By.XPATH, "//div/h2[@class='title text-center']")
if products.is_displayed():
    print("All Products is visible")
else:
    print("All Products is not visible")
driver.find_element(By.XPATH, "//a[@href='/product_details/1']").click()

product_name = driver.find_element(By.XPATH, "//h2[text()='Blue Top']")
category = driver.find_element(By.XPATH,"//p[text()='Category: Women > Tops']")
price = driver.find_element(By.XPATH,"//span[text()='Rs. 500']")
Availability = driver.find_element(By.XPATH,"//p[contains(text(), 'In Stock')]")
condition = driver.find_element(By.XPATH,"//p[contains(text(), 'New')]")
Brand = driver.find_element(By.XPATH,"//p[contains(text(), 'Polo')]")

if product_name.is_displayed():
    print("Blue Top")
else:
    print("Error")
if category.is_displayed():
    print("Women > Tops")
else:
    print("error")
if price.is_displayed():
    print("Rs. 500")
else:
    print("error")
if Availability.is_displayed():
    print("In Stock")
else:
    print("error")
if condition.is_displayed():
    print("New")
else:
    print("error")
if Brand.is_displayed():
    print("polo")
else:
    print("error")