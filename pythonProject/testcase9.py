from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

search_product = "Blue Tshirt"

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
driver.find_element(By.XPATH, "//input[@id = 'search_product']").send_keys(search_product)
driver.find_element(By.XPATH,"//button[@id = 'submit_search']").click()
# time.sleep(5)
# search = driver.find_element(By.XPATH, "//div[@class='single-products']")
# if search.is_displayed():
#     print("search product is visible")
# else:
#     print("search product is not visible")

#last step is doubt