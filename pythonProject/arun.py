from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.get("http://automationexercise.com")
#input functions
Name = "Siva Arun"
email_type = ""
Gender = ""
Email = "pawankalyan18092002@gmail.com"
Password = "Sivaarun@123"
Button = "signup"
Day = "13"
Month = "11"
Year = "2000"
Checkbox = ""
First_Name = "Siva"
Company_Name ="Siva"
Address1 = "Bagmane Tech Park"
Address2 = "Bangalore"
State = "karnataka"
City = "Bangalore"
Pin_Code = "560037"
Mobile_Number = "123456789"
time.sleep(5)
# expected_title="Website for automation practice"
# if driver.title==expected_title:
#     print("home page is visible")
# else:
#     print("home page is not visible")
driver.find_element(By.XPATH, "//a[contains(text(), 'Signup / Login')]").click()
time.sleep(5)
driver.find_element(By.XPATH, f"//input[@name='{Name}']")
time.sleep(5)
driver.find_element(By.XPATH, f"//input[@data-qa='{email_type}-email']").send_keys(Email)
time.sleep(2)
driver.find_element(By.XPATH, f"//button[text()='{Button}']").click()
time.sleep(5)
driver.find_element(By.XPATH, f"//input[@value='{Gender}']").click()
time.sleep(2)
driver.find_element(By.XPATH, f"//input[@id='{Password}']")
time.sleep(2)
driver.find_element(By.XPATH, f"//select[@id='days']/option[@value='{Day}']").click()
time.sleep(2)
driver.find_element(By.XPATH, f"//select[@id='months']/option[@value='{Month}']").click()
time.sleep(2)
driver.find_element(By.XPATH, f"//select[@id='years']/option[@value='{Year}").click()
time.sleep(2)
driver.find_element(By.XPATH, f"//input[@name='{Checkbox}']").click()
time.sleep(2)
driver.find_element(By.ID, "first_name").send_keys(First_Name)
time.sleep(2)
driver.find_element(By.XPATH, f"//input[@id='{Company_Name}']")
time.sleep(2)
driver.find_element(By.XPATH, f"//input[@id='{Address1}']")
time.sleep(2)
driver.find_element(By.ID, "address2").send_keys(Address2)
time.sleep(2)
driver.find_element(By.XPATH, f"//select[@id='country']/option[@value='{Country}']").click()
time.sleep(2)
driver.find_element(By.XPATH, f"//input[@id='{state}']").send_keys(State)
time.sleep(2)
driver.find_element(By.ID, "city").send_keys(City)
time.sleep(2)
driver.find_element(By.ID, "zipcode").send_keys(Pin_Code)
time.sleep(2)
driver.find_element(By.ID, "mobile_number").send_keys(Mobile_Number)
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Create Account']").click()
time.sleep(2)
# driver.find_element(By.ID, "pass").send_keys("dummy@123")
# time.sleep(5)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(5)

# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
# time.sleep(5)
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# time.sleep(5)
# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("Login Success")
# else:
#     print("Login Fail")

# name = 'sivaarun'
# email = 'sivaarun@gmail.com'
# phone = '123456789'
# Address = "Anantapur"
# gender = 'female'
# days = 'sunday'
# country = 'india'
# time.sleep(5)
# driver.find_element(By.ID, "name").send_keys(name)
# time.sleep(5)
# driver.find_element(By.ID, "email").send_keys(email)
# time.sleep(5)
# driver.find_element(By.ID, "phone").send_keys(phone)
# time.sleep(5)
# driver.find_element(By.ID, "textarea").send_keys(Address)
# time.sleep(5)
# driver.find_element(By.XPATH, f"//input[@id='{gender}']").click()
# time.sleep(5)
# driver.find_element(By.XPATH, f"//*[@id='{days}']").click()
# time.sleep(5)
# driver.find_element(By.XPATH, f"//*[@id='{country}").click()
# # driver.find_elements(By.ID, "search-icon-legacy").click()
# # time.sleep(10)
