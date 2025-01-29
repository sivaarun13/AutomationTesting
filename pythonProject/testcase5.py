from selenium import webdriver
from selenium.webdriver.remote.Maintestcase import user

"""
1. Launch browser
2. Navigate to url 'http://automationexercise.com'
3. Verify that home page is visible successfully
4. Click on 'Signup / Login' button
5. Verify 'New User Signup!' is visible
6. Enter name and already registered email address
7. Click 'Signup' button
8. Verify error 'Email Address already exist!' is visible
"""

class Testcase5(user):
    def execute_testcase(self):
        try:
            """Initialize browser"""
            url = "http://automationexercise.com"
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(url)

            """Testcase steps"""
            self.validate_home_page_is_visible_successfully()
            self.click_menu_items('Signup / Login')
            self.validate_New_User_Signup_is_visible()
            self.enter_name("Siva Arun")
            self.enter_Email("pawankalyan18092002@gmail.com", "signup")
            self.submit_button("Signup")
            self.validate_email_address_already_exists()

        except Exception as exp:
            print(f"Error during Test Execution:{exp}")

if __name__ == "__main__":
    testcase = Testcase5()
    testcase.execute_testcase()







































# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# Name = "Siva Arun"
# Email = "pawankalyan18092002@gmail.com"
#
# driver = webdriver.Chrome()
# driver.get("http://automationexercise.com")
# home = driver.find_element(By.XPATH, "//a/img[@alt='Website for automation practice']")
# if home.is_displayed():
#     print('Home page is visible')
# else:
#     print("Home is not visible")
# driver.find_element(By.XPATH, "//a/i[@class='fa fa-lock']").click()
# check = driver.find_element(By.XPATH, "//h2[text()='New User Signup!']")
# if check.is_displayed():
#     print("New User Signup is visible")
# else:
#     print("New User Signup is not visible")
# driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys(Name)
# driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(Email)
# driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
# verify = driver.find_element(By.XPATH, "//p[text()='Email Address already exist!']")
# if verify.is_displayed():
#     print("Email Address already exist! is visible")
# else:
#     print("Email Address already exist! is not visible")